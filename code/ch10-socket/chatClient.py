import socket
import sys

# 服务端主机IP地址和端口号
HOST = '119.23.235.40'#'127.0.0.1'
PORT = 7000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    # 连接服务器
    s.connect((HOST, PORT))
except Exception as e:
    print('Server not found or not open')
    sys.exit()
    
while True:
    c = input('Input the content you want to send:')
    # 发送数据
    s.sendall(c.encode())
    # 从服务端接收数据
    data = s.recv(1024).decode()
    print('Received:', data)
    if c.lower() == 'bye':
        break
# 关闭连接
s.close()
