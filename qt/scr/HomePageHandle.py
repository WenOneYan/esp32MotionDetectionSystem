import copy
import json
from socket import socket
import socket
import time
from PyQt5.QtCore import QThread, QObject, pyqtSignal, Qt
from PyQt5.QtGui import QColor, QBrush
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsTextItem, QGraphicsScene, QVBoxLayout
from HomePage import Ui_mainWindow


# 主页面继承类
class HomePage(QMainWindow, Ui_mainWindow):

    def __init__(self):
        super(HomePage, self).__init__()

        self.UDPserver = None
        self.setupUi(self)

        # 参数初始化
        self.LowerComputerIP = "192.168.229.194"
        self.LowerComputerPort = 1024
        self.LocalIP = "192.168.252.194"
        self.LocalPort = 8080
        # 存储翻滚计算的路径

        self.arr1 = [['A', 'C'], ['D', 'B'], ['E', 'F']]
        self.arr2 = [['A', 'C'], ['D', 'B'], ['E', 'F']]
        self.path = [0]
        self.value = 0

        # 存储平移计算的路径
        self.Displacement_x = []
        self.Displacement_y = []
        # 页面初始化
        self.PageInit()

        # 绑定槽函数
        self.addSensor()

        # 开始监听
        self.ResetButton_clicked()

    # 页面初始化函数
    def PageInit(self):
        print("主页面初始化")
        # 加载ip
        self.getIP()
        # 下位机ip
        self.Edit_IP.setText(str(self.LowerComputerIP))
        self.Edit_Port.setText(str(self.LowerComputerPort))
        # 字体
        self.label_7.setStyleSheet("font-size: 36px; color: red;")
        self.label_8.setStyleSheet("font-size: 36px; color: red;")
        # 未连接
        self.lradioButton_ConnectionStatus.setText("未连接")
        self.lradioButton_ConnectionStatus.setStyleSheet("font-size: 25px; color: red;")

        self.label_18.hide()
        self.label_19.hide()

        # 绘制宫格1
        self.graphicsView.setGeometry(-40, -50, 400, 400)  # 设置位置和大小
        # 去除边框
        self.graphicsView.setStyleSheet("border: 0px;")
        self.scene_2 = QGraphicsScene()
        self.scene_2.setSceneRect(0, 0, 250, 250)
        # 绘制网格，每个宫格大小为50x50
        for i in range(0,321 , 80):
            self.scene_2.addLine(i, 0, i, 320)
            self.scene_2.addLine(0, i, 320, i)
        # 添加数字标识
        for i in range(16):
            text = QGraphicsTextItem(str(i))
            text.setPos((i % 4) * 80 + 15, (3 - i // 4) * 80 + 10)
            text.setScale(1.5)
            self.scene_2.addItem(text)
        self.graphicsView.setScene(self.scene_2)
        layout = QVBoxLayout(self)
        layout.addWidget(self.graphicsView)
        self.setLayout(layout)
        self.graphicsView.setHorizontalScrollBarPolicy(1)  # 去掉水平滚动条
        self.graphicsView.setVerticalScrollBarPolicy(1)  # 去掉垂直滚动条
        self.setMinimumSize(300, 300)  # 设置最小尺寸

        palette = self.graphicsView.palette()
        palette.setColor(self.graphicsView.backgroundRole(), Qt.transparent)
        self.graphicsView.setPalette(palette)


        # 绘制宫格2
        self.graphicsView_2.setGeometry(-40, -50, 400, 400)  # 设置位置和大小
        # 去除边框
        self.graphicsView_2.setStyleSheet("border: 0px;")
        self.scene_2 = QGraphicsScene()
        self.scene_2.setSceneRect(0, 0, 250, 250)
        # 绘制网格，每个宫格大小为50x50
        for i in range(0, 321, 80):
            self.scene_2.addLine(i, 0, i, 320)
            self.scene_2.addLine(0, i, 320, i)
        # 添加数字标识
        for i in range(16):
            text = QGraphicsTextItem(str(i))
            text.setPos((i % 4) * 80 + 15, (3 - i // 4) * 80 + 10)
            text.setScale(1.5)
            self.scene_2.addItem(text)
        self.graphicsView_2.setScene(self.scene_2)
        layout = QVBoxLayout(self)
        layout.addWidget(self.graphicsView_2)
        self.setLayout(layout)
        self.graphicsView_2.setHorizontalScrollBarPolicy(1)  # 去掉水平滚动条
        self.graphicsView_2.setVerticalScrollBarPolicy(1)  # 去掉垂直滚动条
        self.setMinimumSize(300, 300)  # 设置最小尺寸

        palette = self.graphicsView_2.palette()
        palette.setColor(self.graphicsView_2.backgroundRole(), Qt.transparent)
        self.graphicsView_2.setPalette(palette)

    # 绑定槽函数
    def addSensor(self):
        # 复位按键
        self.Tab1_ResetButton.clicked.connect(self.Tab1_ResetButton_clicked)
        self.Tab2_ResetButton.clicked.connect(self.Tab2_ResetButton_clicked)
        self.Tab3_ResetButton.clicked.connect(self.Tab3_ResetButton_clicked)

        # 开始按键
        self.ResetButton.clicked.connect(self.ResetButton_clicked)
        # 退出按键
        self.endButton.clicked.connect(self.endButton_clicked)

        # 开始按钮4
        self.Tab4_StartButton.clicked.connect(self.Tab4_StartButton_clicked)
        # 结束当前任务
        self.TerminatesTheCurrentTask.clicked.connect(self.TerminatesTheCurrentTask_clicked)

    def paint_square(self, view, index, color):
        """
        在给定的 QGraphicsView 中涂色指定的宫格
        view: QGraphicsView 对象
        index: 宫格序号，从 0 到 15
        color: 颜色，接受 Qt 的颜色命名、RGB 数组、RGB16 等方式表示。传入 None 表示清除颜色。
        """
        row = 3 - index // 4  # 计算行数
        col = index % 4  # 计算列数
        rect = view.scene().itemsBoundingRect()  # 获取场景中所有图元的边界矩形
        square_size = rect.width() / 4  # 计算每个宫格的大小
        left = col * square_size + 1  # 左侧坐标
        top = row * square_size + 1  # 顶部坐标

        # 如果传入 None，移除该宫格可能存在的颜色矩形
        if color is None:
            if color is None:
                item = view.scene().itemAt(left, top, view.transform())  # 查找指定位置的图元
            if item is not None:
                view.scene().removeItem(item)  # 如果存在图元，则从场景中移除该图元
        else:
            if isinstance(color, tuple):
                # 如果传入的是 RGB 元组，则使用 QColor.fromRgb() 方法转换为 QColor 实例
                color = QColor.fromRgb(*color)
            elif isinstance(color, str) and color.startswith('#'):
                # 如果传入的是 RGB16 表示方式，则使用 QColor.fromRgbF() 方法转换为 QColor 实例
                color = QColor.fromRgbF(int(color[1:3], 16) / 255.0,
                                        int(color[3:5], 16) / 255.0,
                                        int(color[5:7], 16) / 255.0)
            brush = QBrush(color)  # 创建 QBrush 对象
            view.scene().addRect(left, top, square_size - 2, square_size - 2, brush=brush)  # 在指定位置添加矩形

    def PalaceGridColouring(self, view, index, colors):
        color = QColor(colors)
        color.setAlpha(128)  # 设置透明度为 128，即 50%
        brush = QBrush(color)
        self.paint_square(view, index, brush)

    # 重置当前任务
    def TerminatesTheCurrentTask_clicked(self):
        print("重置当前任务")
        self.LowerComputerIP = self.Edit_IP.text()
        self.LowerComputerPort = self.Edit_Port.text()
        self.UDPserver.SendAMessage("0", self.LowerComputerIP, int(self.LowerComputerPort))

    # 重置按钮槽函数
    def Tab1_ResetButton_clicked(self):
        self.rollPath = []
        self.rollLocation = [0]
        # 更新宫格显示
        # 更新页面显示
        # 更新路径
        self.label_rollLocation.setText('-'.join(str(i) for i in self.rollLocation))

        # 翻滚控制页面重新开始
        # 获取下位机ip/端口
        self.LowerComputerIP = self.Edit_IP.text()
        self.LowerComputerPort = self.Edit_Port.text()
        self.UDPserver.SendAMessage("3", self.LowerComputerIP, int(self.LowerComputerPort))


        # 清空路径
        self.arr1 = [['A', 'C'], ['D', 'B'], ['E', 'F']]
        self.arr2 = [['A', 'C'], ['D', 'B'], ['E', 'F']]
        self.path = [0]
        self.value = 0

        # 清除宫格颜色，循环15次
        for i in range(16):
            self.paint_square(self.graphicsView, i, None)
        for i in range(16):
            self.paint_square(self.graphicsView, i, None)

        self.PalaceGridColouring(self.graphicsView, 0, "green")

    # 重置按钮槽函数
    def Tab2_ResetButton_clicked(self):
        # 重置平移路径
        self.Displacement_x = []
        self.Displacement_y = []
        self.label_TheEndPointOfThePath.setText("待计算")
        # 计算起点
        self.label_ThePathStartPoint.setText("待计算")

        # 平移页面开始
        # 获取下位机ip/端口
        self.LowerComputerIP = self.Edit_IP.text()
        self.LowerComputerPort = self.Edit_Port.text()
        self.UDPserver.SendAMessage("5", self.LowerComputerIP, int(self.LowerComputerPort))

        # 清除宫格颜色，循环15次
        for i in range(16):
            self.paint_square(self.graphicsView_2, i, None)

        # 清除宫格颜色，循环15次
        for i in range(16):
            self.paint_square(self.graphicsView_2, i, None)

    def Tab3_ResetButton_clicked(self):
        # 角度控制页面开始
        # 获取下位机ip/端口
        self.LowerComputerIP = self.Edit_IP.text()
        self.LowerComputerPort = self.Edit_Port.text()
        self.UDPserver.SendAMessage("2", self.LowerComputerIP, int(self.LowerComputerPort))

    # 开始按钮4
    def Tab4_StartButton_clicked(self):
        # 角度控制页面开始
        # 获取下位机ip/端口
        self.LowerComputerIP = self.Edit_IP.text()
        self.LowerComputerPort = self.Edit_Port.text()
        self.UDPserver.SendAMessage("4", self.LowerComputerIP, int(self.LowerComputerPort))

    # 退出按钮
    def endButton_clicked(self):
        # 关闭子进程
        if self.UDPserver is not None and self.UDPserver.isRunning():
            self.UDPserver.terminate()
            self.UDPserver.wait()
        # 关闭UDP套接字
        if self.UDPserver is not None:
            self.UDPserver.close()
            self.UDPserver = None
        # 关闭软件
        QApplication.quit()

    # 开始或重置连接的槽函数
    def ResetButton_clicked(self):
        print("开始或重置连接")


        # 重置连接界面显示
        self.lradioButton_ConnectionStatus.setText("未连接")
        self.lradioButton_ConnectionStatus.setStyleSheet("font-size: 25px; color: red;")
        self.radioButton_RunningStatus.setText("OFF")
        self.radioButton_RunningStatus.setChecked(0)


        # 如果UDP通信子线程已经在运行，则关闭它
        if self.UDPserver is not None and self.UDPserver.isRunning():
            self.UDPserver.terminate()
            self.UDPserver.wait()
        # 关闭UDP套接字
        if self.UDPserver is not None:
            self.UDPserver.close()
            self.UDPserver = None

        # 获取ip和端口
        self.LocalPort = int(self.Local_Port.text())
        # 创建UDP通信对象
        self.UDPserver = UDPserver(self.LocalIP, self.LocalPort)
        # 绑定信号槽函数
        self.UDPserver.receivedData.connect(self.handleReceivedData)
        self.UDPserver.connection_signal.connect(self.updataState)

        # 发送连接标志
        self.LowerComputerIP = self.Edit_IP.text()
        self.LowerComputerPort = self.Edit_Port.text()
        self.UDPserver.SendAMessage("0", self.LowerComputerIP, int(self.LowerComputerPort))

        # 开启连接侦听
        self.UDPserver.checkTimeout()
        # 重新开始接收数据
        self.UDPserver.start()

    # 接收数据
    def handleReceivedData(self, data, addr):
        print(f"Received {len(data)} bytes from {addr}: {data}")
        self.Edit_IP.setText(addr[0])
        self.Edit_Port.setText(str(addr[1]))

        # 在这里执行界面更新操作
        data_dict = json.loads(data)

        print(data_dict)
        # 更新开关状态
        if data_dict["id"] == "1":
            print("更新开关状态!")
            if data_dict["data"] == "0":
                self.radioButton_RunningStatus.setText("OFF")
                self.radioButton_RunningStatus.setChecked(0)
            if data_dict["data"] == "1":
                self.radioButton_RunningStatus.setText("ON")
                self.radioButton_RunningStatus.setChecked(1)
            return

        # 更新角度信息
        if data_dict["id"] == "2":
            self.Data_a.setText(str(data_dict["data_a"]))
            self.Data_b.setText(str(data_dict["data_b"]))
            return
        # 更新翻滚测试信息
        if data_dict["id"] == "3":
            print("拿到翻滚数据:", data_dict["data"])
            self.label_8.setText(str(data_dict["data"]))
            # 计算位置变化信息
            self.CalculateTheRollPath(data_dict["data"])
            return

        # 更新朝上面数据信息
        if data_dict["id"] == "4":
            print("朝上面数据:", data_dict["data"])
            self.label_7.setText(str(data_dict["data"]))
            return

        # 更新平移数据信息
        if data_dict["id"] == "5":
            if data_dict["status"] == "0":
                print("平移数据信息:", data_dict["data_x"], data_dict["data_y"])
                print("追加数据")
                self.Displacement_x.append(int(data_dict["data_x"]))
                self.Displacement_y.append(int(data_dict["data_y"]))
                return
            if data_dict["status"] == "1":
                # 一次平移结束,开始计算平移路径
                if self.Displacement_x != [] and self.Displacement_y != []:
                    self.CalculateTheDisplacementPath()

    # 计算翻滚路径
    def CalculateTheRollPath(self, data):
        self.arr2[0][0] = data
        if data == self.arr1[1][0]:
            self.value += 1
            self.path.append(self.value)
            self.arr2[0][1] = self.arr1[1][1]
            self.arr2[1][0] = self.arr1[0][1]
            self.arr2[1][1] = self.arr1[0][0]
            self.arr2[2] = self.arr1[2]

        elif data == self.arr1[1][1]:
            self.value -= 1
            self.path.append(self.value)
            self.arr2[0][1] = self.arr1[1][0]
            self.arr2[1][0] = self.arr1[0][0]
            self.arr2[1][1] = self.arr1[0][1]
            self.arr2[2] = self.arr1[2]

        elif data == self.arr1[2][0]:
            self.value += 4
            self.path.append(self.value)
            self.arr2[0][1] = self.arr1[2][1]
            self.arr2[1] = self.arr1[1]
            self.arr2[2][0] = self.arr1[0][1]
            self.arr2[2][1] = self.arr1[0][0]

        elif data == self.arr1[2][1]:
            self.value -= 4
            self.path.append(self.value)
            self.arr2[0][1] = self.arr1[2][0]
            self.arr2[1] = self.arr1[1]
            self.arr2[2][0] = self.arr1[0][0]
            self.arr2[2][1] = self.arr1[0][1]

        self.arr1 = copy.deepcopy(self.arr2)

        print(self.path)

        # 更新页面显示
        # 路径
        ch ="-"
        self.label_rollLocation.setText(ch.join(str(x) for x in self.path))
        # 位置
        if self.path != [] and  0 < self.path[-1] < 16:
            self.PalaceGridColouring(self.graphicsView, self.path[-1], "green")




    # 计算平移起点
    def CalculateTheDisplacementStart(self, theEnd, VarDisplacement_x, VarDisplacement_y):
        print("计算平移起点")
        # 界面显示终点
        if theEnd == "右上":
            self.label_TheEndPointOfThePath.setText("15")
            # 计算起点
            Thestart = 15 - (VarDisplacement_x + VarDisplacement_y)
            self.label_ThePathStartPoint.setText(str(Thestart))
            self.PalaceGridColouring(self.graphicsView_2, Thestart, "green")
            self.PalaceGridColouring(self.graphicsView_2, 15, "red")

        if theEnd == "右下":
            self.label_TheEndPointOfThePath.setText("03")
            Thestart = 3 - (VarDisplacement_x + VarDisplacement_y)
            self.label_ThePathStartPoint.setText(str(Thestart))
            self.PalaceGridColouring(self.graphicsView_2, Thestart, "green")
            self.PalaceGridColouring(self.graphicsView_2, 3, "red")

        if theEnd == "左上":
            self.label_TheEndPointOfThePath.setText("12")
            Thestart = 12 - (VarDisplacement_x + VarDisplacement_y)
            self.label_ThePathStartPoint.setText(str(Thestart))
            self.PalaceGridColouring(self.graphicsView_2, Thestart, "green")
            self.PalaceGridColouring(self.graphicsView_2, 12, "red")

        if theEnd == "左下":
            self.label_TheEndPointOfThePath.setText("00")
            Thestart = 00 - (VarDisplacement_x + VarDisplacement_y)
            self.label_ThePathStartPoint.setText(str(Thestart))
            self.PalaceGridColouring(self.graphicsView_2, Thestart, "green")
            self.PalaceGridColouring(self.graphicsView_2, 00, "red")

    # 更新下位机状态
    def updataState(self, state):
        print("更新下位机状态")
        if state == "offline":
            self.lradioButton_ConnectionStatus.setText("未连接")
            self.lradioButton_ConnectionStatus.setStyleSheet("font-size: 20px; color: red;")

        elif state == "online":
            print("已连接")
            self.lradioButton_ConnectionStatus.setText("已连接")
            self.lradioButton_ConnectionStatus.setStyleSheet("font-size: 20px; color: green;")

    # 获取本机ip
    def getIP(self):
        print("获取本机IP")
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        print("本机IP地址为：", ip)
        self.LocalIP = ip
        # 更新ui显示ip
        self.label_IP.setText(ip)
        # 更新端口显示
        self.Local_Port.setText(str(self.LocalPort))
        s.close()

    # 计算平移路径
    def CalculateTheDisplacementPath(self):
        print("计算平移路径")
        print("x:" + str(self.Displacement_x), "y:" + str(self.Displacement_y))
        VarDisplacement_x = sum(self.Displacement_x)
        VarDisplacement_y = sum(self.Displacement_y)
        TheEnd = "TheEnd"
        print("x变化量:" + str(VarDisplacement_x), "y变化量:" + str(VarDisplacement_y))

        # 当两个变化量均不为0时:
        if VarDisplacement_x != 0 and VarDisplacement_y != 0:
            if VarDisplacement_x > 0 and VarDisplacement_y > 0:
                # 右上
                print("右上")
                TheEnd = "右上"

            if VarDisplacement_x > 0 and VarDisplacement_y < 0:
                # 右下
                print("右下")
                TheEnd = "右下"

            if VarDisplacement_x < 0 and VarDisplacement_y > 0:
                # 左上
                print("左上")
                TheEnd = "左上"

            if VarDisplacement_x < 0 and VarDisplacement_y < 0:
                # 左下
                print("左下")
                TheEnd = "左下"
            # 计算起始位置
            self.CalculateTheDisplacementStart(TheEnd, VarDisplacement_x, VarDisplacement_y)

        # 当两个变化量有一个为0时:
        if VarDisplacement_x == 0 or VarDisplacement_y == 0:
            print("有一个为0")
            # 当两个变化量均为0时:
            if VarDisplacement_x == 0 and VarDisplacement_y == 0:
                x = next((x for x in self.Displacement_x if x != 0), 0)
                y = next((y for y in self.Displacement_y if y != 0), 0)
                print("x:" + str(x), "y:" + str(y))
                if x > 0 and y > 0:
                    # 左下
                    self.label_TheEndPointOfThePath.setText("00")
                    self.label_ThePathStartPoint.setText(str(00))
                    self.PalaceGridColouring(self.graphicsView_2, 00, "red")

                elif x > 0 and y < 0:
                    # 左上
                    self.label_TheEndPointOfThePath.setText("12")
                    self.label_ThePathStartPoint.setText(str(12))
                    self.PalaceGridColouring(self.graphicsView_2, 12, "red")

                elif x < 0 and y > 0:
                    # 右下
                    self.label_TheEndPointOfThePath.setText("3")
                    self.label_ThePathStartPoint.setText(str(3))
                    self.PalaceGridColouring(self.graphicsView_2, 3, "red")

                elif x < 0 and y < 0:
                    # 右上
                    self.label_TheEndPointOfThePath.setText("15")
                    self.label_ThePathStartPoint.setText(str(15))
                    self.PalaceGridColouring(self.graphicsView_2, 15, "red")

                elif x == 0:
                    if y > 0:
                        self.label_TheEndPointOfThePath.setText("00/3")
                        Thestarta = 00 - (VarDisplacement_x + VarDisplacement_y)
                        Thestartb = 3 - (VarDisplacement_x + VarDisplacement_y)
                        self.label_ThePathStartPoint.setText(str(Thestarta) + "/" + str(Thestartb))

                        # 绘制路径
                        self.PalaceGridColouring(self.graphicsView_2, 00, "green")
                        self.PalaceGridColouring(self.graphicsView_2, 3, "green")
                        self.PalaceGridColouring(self.graphicsView_2, Thestarta, "red")
                        self.PalaceGridColouring(self.graphicsView_2, Thestartb, "red")

                    elif y < 0:
                        self.label_TheEndPointOfThePath.setText("12/15")
                        Thestarta = 12 - (VarDisplacement_x + VarDisplacement_y)
                        Thestartb = 15 - (VarDisplacement_x + VarDisplacement_y)
                        self.label_ThePathStartPoint.setText(str(Thestarta) + "/" + str(Thestartb))

                        # 绘制路径
                        self.PalaceGridColouring(self.graphicsView_2, 12, "green")
                        self.PalaceGridColouring(self.graphicsView_2, 15, "green")
                        self.PalaceGridColouring(self.graphicsView_2, Thestarta, "red")
                        self.PalaceGridColouring(self.graphicsView_2, Thestartb, "red")

                elif y == 0:
                    if x < 0:
                        self.label_TheEndPointOfThePath.setText("3/15")
                        Thestarta = 3 - (VarDisplacement_x + VarDisplacement_y)
                        Thestartb = 15 - (VarDisplacement_x + VarDisplacement_y)
                        self.label_ThePathStartPoint.setText(str(Thestarta) + "/" + str(Thestartb))

                        # 绘制
                        self.PalaceGridColouring(self.graphicsView_2, 3, "green")
                        self.PalaceGridColouring(self.graphicsView_2, 15, "green")
                        self.PalaceGridColouring(self.graphicsView_2, Thestarta, "red")
                        self.PalaceGridColouring(self.graphicsView_2, Thestartb, "red")
                    elif x > 0:
                        self.label_TheEndPointOfThePath.setText("00/12")
                        Thestarta = 00 - (VarDisplacement_x + VarDisplacement_y)
                        Thestartb = 12 - (VarDisplacement_x + VarDisplacement_y)
                        self.label_ThePathStartPoint.setText(str(Thestarta) + "/" + str(Thestartb))

                        # 绘制
                        self.PalaceGridColouring(self.graphicsView_2, 00, "green")
                        self.PalaceGridColouring(self.graphicsView_2, 12, "green")
                        self.PalaceGridColouring(self.graphicsView_2, Thestarta, "red")
                        self.PalaceGridColouring(self.graphicsView_2, Thestartb, "red")

            if VarDisplacement_x == 0 and VarDisplacement_y > 0:
                # 上
                x = next((x for x in self.Displacement_x if x != 0), None)
                if x == None:
                    self.label_TheEndPointOfThePath.setText("12/15")
                    Thestarta = 12 - (VarDisplacement_x + VarDisplacement_y)
                    Thestartb = 15 - (VarDisplacement_x + VarDisplacement_y)
                    self.label_ThePathStartPoint.setText(str(Thestarta) + "/" + str(Thestartb))

                    # 绘制
                    self.PalaceGridColouring(self.graphicsView_2, 12, "green")
                    self.PalaceGridColouring(self.graphicsView_2, 15, "green")
                    self.PalaceGridColouring(self.graphicsView_2, Thestarta, "red")
                    self.PalaceGridColouring(self.graphicsView_2, Thestartb, "red")
                elif x > 0:
                    # 终点
                    self.label_TheEndPointOfThePath.setText("12")
                    Thestart = 12 - (VarDisplacement_x + VarDisplacement_y)
                    self.label_ThePathStartPoint.setText(str(Thestart))

                    # 绘制
                    self.PalaceGridColouring(self.graphicsView_2, 12, "green")
                    self.PalaceGridColouring(self.graphicsView_2, Thestart, "red")

                elif x < 0:
                    # 终点
                    self.label_TheEndPointOfThePath.setText("15")
                    Thestart = 15 - (VarDisplacement_x + VarDisplacement_y)
                    self.label_ThePathStartPoint.setText(str(Thestart))

                    # 绘制
                    self.PalaceGridColouring(self.graphicsView_2, 15, "green")
                    self.PalaceGridColouring(self.graphicsView_2, Thestart, "red")

            if VarDisplacement_x == 0 and VarDisplacement_y < 0:
                x = next((x for x in self.Displacement_x if x != 0), None)

                if x == None:
                    self.label_TheEndPointOfThePath.setText("00/3")
                    Thestarta = 00 - (VarDisplacement_x + VarDisplacement_y)
                    Thestartb = 3 - (VarDisplacement_x + VarDisplacement_y)
                    self.label_ThePathStartPoint.setText(str(Thestarta) + "/" + str(Thestartb))

                    # 绘制
                    self.PalaceGridColouring(self.graphicsView_2, 00, "green")
                    self.PalaceGridColouring(self.graphicsView_2, 3, "green")
                    self.PalaceGridColouring(self.graphicsView_2, Thestarta, "red")
                    self.PalaceGridColouring(self.graphicsView_2, Thestartb, "red")
                elif x > 0:
                    # 终点
                    self.label_TheEndPointOfThePath.setText("00")
                    Thestart = 00 - (VarDisplacement_x + VarDisplacement_y)
                    self.label_ThePathStartPoint.setText(str(Thestart))

                    # 绘制
                    self.PalaceGridColouring(self.graphicsView_2, 00, "green")
                    self.PalaceGridColouring(self.graphicsView_2, Thestart, "red")

                elif x < 0:
                    # 终点
                    self.label_TheEndPointOfThePath.setText("3")
                    Thestart = 3 - (VarDisplacement_x + VarDisplacement_y)
                    self.label_ThePathStartPoint.setText(str(Thestart))

                    # 绘制
                    self.PalaceGridColouring(self.graphicsView_2, 3, "green")
                    self.PalaceGridColouring(self.graphicsView_2, Thestart, "red")

            if VarDisplacement_x > 0 and VarDisplacement_y == 0:
                # 右
                print("右")
                y = next((x for x in self.Displacement_y if x != 0), None)
                if y == None:
                    self.label_TheEndPointOfThePath.setText("3/15")
                    Thestarta = 3 - (VarDisplacement_x + VarDisplacement_y)
                    Thestartb = 15 - (VarDisplacement_x + VarDisplacement_y)
                    self.label_ThePathStartPoint.setText(str(Thestarta) + "/" + str(Thestartb))

                    # 绘制
                    self.PalaceGridColouring(self.graphicsView_2, 3, "green")
                    self.PalaceGridColouring(self.graphicsView_2, 15, "green")
                    self.PalaceGridColouring(self.graphicsView_2, Thestarta, "red")
                    self.PalaceGridColouring(self.graphicsView_2, Thestartb, "red")
                elif y > 0:
                    # 终点
                    self.label_TheEndPointOfThePath.setText("3")
                    Thestart = 3 - (VarDisplacement_x + VarDisplacement_y)
                    self.label_ThePathStartPoint.setText(str(Thestart))

                    # 绘制
                    self.PalaceGridColouring(self.graphicsView_2, 3, "green")
                    self.PalaceGridColouring(self.graphicsView_2, Thestart, "red")

                elif y < 0:
                    # 终点
                    self.label_TheEndPointOfThePath.setText("15")
                    Thestart = 15 - (VarDisplacement_x + VarDisplacement_y)
                    self.label_ThePathStartPoint.setText(str(Thestart))

                    # 绘制
                    self.PalaceGridColouring(self.graphicsView_2, 15, "green")
                    self.PalaceGridColouring(self.graphicsView_2, Thestart, "red")

            if VarDisplacement_x < 0 and VarDisplacement_y == 0:
                # 左
                print("左")
                y = next((x for x in self.Displacement_y if x != 0), None)
                if y == None:
                    self.label_TheEndPointOfThePath.setText("00/12")
                    Thestarta = 00 - (VarDisplacement_x + VarDisplacement_y)
                    Thestartb = 12 - (VarDisplacement_x + VarDisplacement_y)
                    self.label_ThePathStartPoint.setText(str(Thestarta) + "/" + str(Thestartb))

                    # 绘制
                    self.PalaceGridColouring(self.graphicsView_2, 00, "green")
                    self.PalaceGridColouring(self.graphicsView_2, 12, "green")
                    self.PalaceGridColouring(self.graphicsView_2, Thestarta, "red")
                    self.PalaceGridColouring(self.graphicsView_2, Thestartb, "red")
                elif y > 0:
                    # 终点
                    self.label_TheEndPointOfThePath.setText("00")
                    Thestart = 00 - (VarDisplacement_x + VarDisplacement_y)
                    self.label_ThePathStartPoint.setText(str(Thestart))

                    # 绘制
                    self.PalaceGridColouring(self.graphicsView_2, 00, "green")
                    self.PalaceGridColouring(self.graphicsView_2, Thestart, "red")

                elif y < 0:
                    # 终点
                    self.label_TheEndPointOfThePath.setText("12")
                    Thestart = 12 - (VarDisplacement_x + VarDisplacement_y)
                    self.label_ThePathStartPoint.setText(str(Thestart))

                    self.PalaceGridColouring(self.graphicsView_2, 12, "green")
                    self.PalaceGridColouring(self.graphicsView_2, Thestart, "red")


# UDP通信类
class UDPserver(QThread, QObject):
    # 自定义信号用于向主线程传递数据
    receivedData = pyqtSignal(bytes, tuple)
    connection_signal = pyqtSignal(str)

    def __init__(self, ip, port):
        super().__init__()
        self.ip = ip
        self.port = port
        print("UDP通信初始化")

        # 初始化计时器（初始时间为当前时间）
        self.timer = time.time()

        # 创建UDP套接字并绑定到本地地址和端口
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        except socket.error as e:
            print("无法创建UDP套接字: {}".format(e))
            return
        # 打印本机ip
        print("监听端口", str(port))
        # 绑定本地IP和端口号
        try:
            self.sock.bind((self.ip, self.port))
        except socket.error as e:
            print("无法绑定UDP套接字: {}".format(e))
            self.sock.close()
            return

    # 接收数据线程
    def run(self):
        while True:
            data, addr = self.sock.recvfrom(1024)
            # 更新计时器
            self.timer = time.time()
            # 更新状态
            self.connection_signal.emit("online")
            self.receivedData.emit(data, addr)

    def checkTimeout(self):
        # 检查计时器是否超过30秒
        if (time.time() - self.timer) > 30:
            # 如果超过30秒，更新下位机状态指示符
            print("30秒内无数据，下位机处于离线状态")
            self.connection_signal.emit("offline")
        else:
            pass
            # 否则，等待一段时间后再次检查
            # self.checkTimeout()

    def SendAMessage(self, str, dest_ip, dest_port):
        # 将字符串转换为bytes类型
        data = str.encode('utf-8')
        # 使用套接字发送数据
        try:
            self.sock.sendto(data, (dest_ip, dest_port))
            print("已发送数据到{}:{}".format(dest_ip, dest_port))
        except socket.error as e:
            print("发送数据失败: {}".format(e))

    # 关闭套接字
    def close(self):
        self.sock.close()
