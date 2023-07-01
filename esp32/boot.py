from machine import Pin, I2C, SoftI2C
from socket import *
import time
from time import sleep
import struct
import network
import math
# 字符转JSON
import ujson
# 多线程模块
import _thread
# OLED屏幕模块
import ssd1306


# OLED 设置引脚
i2c = SoftI2C(scl=Pin(0), sda=Pin(4))
# 宽度高度
oled_width = 128
oled_height = 64

# 创建oled屏幕对象
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# 在指定位置处显示文字
oled.text('ESP32...', 0, 0)
oled.show()

# pin2 Esp32板载led
pin2 = Pin(2, Pin.OUT)
# pin3 有源蜂鸣器 设置负极引脚 正级接电源
pin3 = Pin(26, Pin.OUT)
pin3.value(1)
pin2.value(0)

# MPU6050 I2C 地址
MPU6050_ADDR = 0x68

# MPU6050 三轴加速度寄存器地址 本题只用了三轴加速度
MPU6050_ACCEL_XOUT_H = 0x3B
MPU6050_ACCEL_YOUT_H = 0x3D
MPU6050_ACCEL_ZOUT_H = 0x3F

# 设置 mpu6050 I2C引脚
i2c = I2C(0, scl=Pin(5), sda=Pin(18), freq=100000)

# 初始化 MPU6050
i2c.writeto_mem(MPU6050_ADDR, 0x6B, b'\x00')

# 三轴误差值记录
error_x = 0
error_y = 0
error_z = 0

# 灯状态
string = "OFF"
flag = 1
id = 1

# 创建udp套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)

# 从所有端口找到空闲端口
for port in range(1024, 65536):
    try:
        udp_socket.bind(("0.0.0.0", port))
        break
    except OSError:
        pass

# 上位机ip
dest_addr = ''

# 显示输出端口号
# print("Local IP address:", local_ip)
# print("Local port:", port)

# 链接WiFi
def do_connect():
    global udp_socket
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        # 设置热点名称 密码 注意热点要改成2.4G
        wlan.connect('AAA', '12345678')
        i = 1
        while not wlan.isconnected():
            print("正在连接...{}".format(i))
            i += 1
            time.sleep(1)
    print('network config:', wlan.ifconfig())
    # 显示自身IP 开启端口号
    oled.text('IP:', 0, 10)
    oled.text(wlan.ifconfig()[0], 6, 22)
    oled.text('port:', 0, 34)
    oled.text(str(port), 45, 34)
    oled.show()
    # 蜂鸣器提示
    buzzer(0.5)


def buzzer(data):
    pin3.value(0)
    time.sleep(data)
    pin3.value(1)
    

# 消除初始误差
def calculation_error():
    i = 20
    global error_x, error_y, error_z
    error_x, error_y, error_z = 0, 0, 0
    if i:
        i -= 1
        # 读取当前三轴加速度
        accel_x, accel_y, accel_z = read_mpu6050()

        # 累加2s内的20次
        error_x += accel_x
        error_y += accel_y
        error_z += 0.98 - accel_z
        time.sleep(0.1)
        if i == 0:
            # 计算均值为误差值
            error_x = error_x / 20
            error_y = error_y / 20
            error_z = error_z / 20


# 读取三轴加速度
def read_mpu6050():
    global i2c

    # 轴向加速度
    # 读取高位和低位数值 获取到数组
    accel_x = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_ACCEL_XOUT_H, 2)
    accel_y = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_ACCEL_YOUT_H, 2)
    accel_z = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_ACCEL_ZOUT_H, 2)

    # 数组拼接 转为有符号整型 最高位为符号位 要注意负数的反码 补码
    accel_x = (accel_x[0] << 8) | accel_x[1]
    if accel_x & (1 << 15):
        accel_x = -((accel_x ^ 0xFFFF) + 1)
    accel_y = (accel_y[0] << 8) | accel_y[1]
    if accel_y & (1 << 15):
        accel_y = -((accel_y ^ 0xFFFF) + 1)
    accel_z = (accel_z[0] << 8) | accel_z[1]
    if accel_z & (1 << 15):
        accel_z = -((accel_z ^ 0xFFFF) + 1)

    # 除以2的16次方或15次方 (实际只有15位有效数据 最高位符号位已左移为0)
    accel_x = accel_x / 16384.0
    accel_y = accel_y / 16384.0
    accel_z = accel_z / 16384.0
    
    return accel_x, accel_y, accel_z


# 消除初始偏移后数据
def after_value():
    global error_x, error_y, error_z
    
    accel_x, accel_y, accel_z = read_mpu6050()
    # 原始数据实测x y z加速度分别比理论值0 0 0.98 小 小 大
    # 可改为判断来决定+- 对本题影响不大
    accel_x -= error_x
    accel_y -= error_y
    accel_z += error_z
    
    return accel_x, accel_y, accel_z


# 控制运行状态
def on_off():
    global string, flag

    while True:
        ax, ay, az = after_value()

        # 测试三轴加速度和大于2(经验值)
        if abs(ax) + abs (ay) + abs(az) > 2:
            print(str(ax) + ' ' + str(ay) + ' ' + str(az))
            if string == "OFF":
                string = "ON"
                send_data(1, 1)
                pin2.value(1)
                print(string)
                # break
            else:
                string = "OFF"
                send_data(1, 0)
                print(string)
                pin2.value(0)
                # break
        if flag == 0:
            break
        time.sleep(0.1)
    

# 测试角度
def tilt_angle():
    global flag
    arr = [[0 for j in range(2)] for i in range(10)]
    while True:
        aax, aay, aaz = after_value()
        # print(str(aax) + ' '+str(aay)+' ' + str(aaz))
        
        result_rad_a = math.atan(aax / aaz)
        result_rad_b = math.atan(aay / aaz)
        result_deg_a = math.degrees(result_rad_a)
        result_deg_b = math.degrees(result_rad_b)
        
        arr.pop(0)
        
        arr.append([result_deg_a, result_deg_b])
        result_deg_a = round(sum(arr0[0] for arr0 in arr) / 10, 2)
        result_deg_b = round(sum(arr1[1] for arr1 in arr) / 10, 2)
        # print(str(abs(round(result_deg_a, 2))) + ' ' + str(abs(round(result_deg_b, 2))))
        
        tilt_angle_send_data(result_deg_a, result_deg_b)
        if flag == 0:
            buzzer(0.5)
            break
        time.sleep(0.001)


# 测试当前向上面
def now_surface():
    global id
    now_face = ""
    ax, ay, az = after_value()
    print(str(ax) + ' ' + str(ay) + ' ' + str(az))
    if abs(ax) > 0.8:
        if ax > 0:
            now_face = "D"
        else:
            now_face = "B"
    elif abs(ay) > 0.8:
        if ay > 0:
            now_face = "E"
        else:
            now_face = "F"
    elif abs(az) > 0.8:
        if az > 0:
            now_face = "A"
        else:
            now_face = "C"
    send_data(4, now_face)
    id = 0
    

# 翻滚测试
def surface():
    global flag
    old_face = ""
    new_face = "A"
    axyz_arr = [[0 for j in range(3)] for i in range(5)]
    while True:
        ax, ay, az = after_value()
        axyz_arr.pop(0)
        axyz_arr.append([ax, ay, az])
        aax = sum(arr0[0] for arr0 in axyz_arr) / 5
        aay = sum(arr1[1] for arr1 in axyz_arr) / 5
        aaz = sum(arr2[2] for arr2 in axyz_arr) / 5
        if abs(aax) > 0.9:
            if aax > 0:
                new_face = "D"
            else:
                new_face = "B"
        elif abs(aay) > 0.9:
            if aay > 0:
                new_face = "E"
            else:
                new_face = "F"
        elif abs(aaz) > 0.9:
            if aaz > 0:
                new_face = "A"
            else:
                new_face = "C"
        if old_face != new_face:
            old_face = new_face
            print_face(old_face)
            send_data(3, old_face)
            buzzer(0.2)
        if flag == 0:
            buzzer(0.5)
            break
        time.sleep(0.1)
        

# 接受上位机数据 非阻塞udp接受
def recv_data():
    global udp_socket, flag, id
    udp_socket.setblocking(False)
    while True:
        try:
            data, addr = udp_socket.recvfrom(1024)
            id = data.decode("utf-8")
            id = int(id)
            flag = 0
            if id == 0:
                print("退出")
                break
            else:
                print("其他程序")
                break
        except OSError:
            pass


# 平移测试
def box_path():
    global flag
    accel = 0.2
    axyz_arr = [[0 for j in range(2)] for i in range(30)]
    while True:
        ax, ay, az = after_value()
        ax, ay = round(ax, 2), round(ay, 2)
        axyz_arr.pop(0)
        axyz_arr.append([ax, ay])
        ax = round(sum(arr0[0] for arr0 in axyz_arr) / 30, 2)
        ay = round(sum(arr1[1] for arr1 in axyz_arr) / 30, 2)
        print(str(ax) + ' ' + str(ay))
        if ax > accel:
            print("向左")
            box_path_send_data(-1, 0)
            buzzer(0.2)
            axyz_arr = [[0 for j in range(2)] for i in range(30)]
            time.sleep(0.5)
        elif ax < -accel:
            print("向右")
            box_path_send_data(1, 0)
            buzzer(0.2)
            axyz_arr = [[0 for j in range(2)] for i in range(30)]
            time.sleep(0.5)
        elif ay > accel:
            print("向后")
            box_path_send_data(0, -4)
            buzzer(0.2)
            axyz_arr = [[0 for j in range(2)] for i in range(30)]
            time.sleep(0.5)
        elif ay < -accel:
            print("向前")
            box_path_send_data(0, 4)
            buzzer(0.2)
            axyz_arr = [[0 for j in range(2)] for i in range(30)]
            time.sleep(0.5)
        if flag == 0:
            box_path_send_data(0, 0)
            buzzer(0.5)
            break


def print_face(face):
    print(face)


def tilt_angle_send_data(result_deg_a, result_deg_b):
    global udp_socket, dest_addr

    result_deg_a, result_deg_b = str(result_deg_a), str(result_deg_b)

    dest_addr = (dest_addr)

    data = {
        "id": id,
        "data_a": result_deg_a,
        "data_b": result_deg_b
    }
    json_str = ujson.dumps(data)
    json_str = str(json_str)
    # 单引号变双引号
    json_str = json_str.replace("'", '"')

    # 发送数据到指定的电脑上
    udp_socket.sendto(json_str.encode('utf-8'), dest_addr)


def send_data(id, data):
    global udp_socket, dest_addr

    id, data = str(id), str(data)
    dest_addr = (dest_addr)

    data = {
        "id": id,
        "data": data
    }
    json_str = ujson.dumps(data)
    json_str = str(json_str)
    # 单引号变双引号
    json_str = json_str.replace("'", '"')

    # 发送数据到指定的电脑上
    udp_socket.sendto(json_str.encode('utf-8'), dest_addr)


def box_path_send_data(data_x, data_y):
    global udp_socket, dest_addr

    id, status = '5', '0'
    if data_x + data_y == 0:
        # 结束标识
        status = '1'
    # 转字符 已知软件开发用的JSON格式数据 规范习惯
    data_x, data_y = str(data_x), str(data_y)

    # 接收方的地址
    dest_addr = (dest_addr)

    data = {
        "id": id,
        "status": status,
        "data_x": data_x,
        "data_y": data_y
    }
    json_str = ujson.dumps(data)
    json_str = str(json_str)
    # 单引号变双引号
    json_str = json_str.replace("'", '"')
        
    # 发送数据到指定的电脑上
    udp_socket.sendto(json_str.encode('utf-8'), dest_addr)
    
    

def main():
    global udp_sockst, flag, id, dest_addr, dest_port, string
    # 链接WiFi
    do_connect()

    # udp_socket.setblocking(True)
    data, addr = udp_socket.recvfrom(1024)
    dest_addr = addr
    
    buzzer(0.2)
    
    calculation_error()

    # 发送OFF
    send_data(1, 0)
    
    id = 0
    while True:

        if id == 0:
            print("基础一")
            flag = 1
            _thread.start_new_thread(recv_data, ())
            _thread.start_new_thread(on_off, ())
            while True:
                if flag == 0:
                    break
        elif id == 2:
            print("基础二")
            buzzer(0.5)
            flag = 1
            calculation_error()
            _thread.start_new_thread(recv_data, ())
            _thread.start_new_thread(tilt_angle, ())
            while True:
                if flag == 0:
                    break
        elif id == 4:
            buzzer(0.5)
            print("基础三")
            now_surface()
        elif id == 3:
            buzzer(0.5)
            print("发挥一")
            flag = 1
            calculation_error()
            _thread.start_new_thread(recv_data, ())
            _thread.start_new_thread(surface, ())
            while True:
                if flag == 0:
                    break
        elif id == 5:
            buzzer(0.5)
            print("发挥二")
            flag = 1
            calculation_error()
            _thread.start_new_thread(recv_data, ())
            _thread.start_new_thread(box_path, ())
            while True:
                if flag == 0:
                    break
        time.sleep(0.1)


if __name__ == "__main__":
    main()

