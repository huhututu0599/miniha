import socket

# 定义服务器地址和端口号
SERVER_HOST = '0.0.0.0'  # 监听所有可用的网络接口
SERVER_PORT = 9211

# 创建TCP套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定服务器地址和端口号
server_socket.bind((SERVER_HOST, SERVER_PORT))

# 开始监听传入的连接请求
server_socket.listen(5)
print(f"[*] Listening on {SERVER_HOST}:{SERVER_PORT}")

while True:
    # 接受客户端连接
    client_socket, client_address = server_socket.accept()
    print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")

    while True:
        # 从客户端接收数据
        data = client_socket.recv(1024)
        if data:
            print(f"[*] Received data: {data.decode()}")

            # 如果收到的数据是"close"，则关闭连接
            if data.decode() == "close":
                print("[*] Closing connection")
                break

            # 将收到的数据发送回客户端
            client_socket.sendall(b"Server received your message. Thank you!")

    # 关闭客户端套接字
    client_socket.close()
