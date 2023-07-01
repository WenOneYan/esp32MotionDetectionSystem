import socket



# 创建UDP套接字
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定本地IP和端口号
local_ip = '192.168.63.109'
local_port = 8089

sock.bind((local_ip, local_port))

# 接收数据
while True:
    data, addr = sock.recvfrom(1024)
    print(f"Received {len(data)} bytes from {addr}: {data}")
