import tkinter as tk
import socket

def connect_to_server():
    global client_socket
    SERVER_HOST = '192.168.124.8'
    SERVER_PORT = 8100
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        print("Connected to server")
    except Exception as e:
        print("Failed to connect to server:", e)

def send_data_to_server():
    data = text_entry.get()
    if client_socket:
        client_socket.sendall(data.encode())
        print("Data sent to server:", data)


def close_to_server():
    # 关闭客户端套接字
    client_socket.close()
    print("Data sent to server:")

# 创建主窗口
root = tk.Tk()
root.title("TCP Client")

# 设置窗口大小
root.geometry("800x600")

# 创建文本框
text_entry = tk.Entry(root)
text_entry.pack()

# 创建按钮1，连接到服务器
connect_button = tk.Button(root, text="Connect to Server", command=connect_to_server)
connect_button.pack()

# 创建按钮2，发送数据到服务器
send_button = tk.Button(root, text="Send Data to Server", command=send_data_to_server)
send_button.pack()

# 创建按钮2，发送数据到服务器
send_button = tk.Button(root, text="Close to Server", command=close_to_server)
send_button.pack()

# 启动主循环
root.mainloop()
