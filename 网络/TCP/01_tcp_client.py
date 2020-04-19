import socket



def main():
    # 1.创建TCP套接字
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 2.链接服务器
    server_ip = input("请输入服务器ip:")
    server_port = int(input("请输入服务器port:"))
    server_addr = (server_ip,server_port)
    tcp_socket.connect(server_addr)
    # tcp_socket.connect(("192.168.1.1.=",8080))

    # 3.接收/发送数据
    # 发送
    send_data = input("请输入要发送的数据:")
    tcp_socket.send(send_data.encode("utf-8"))
    # 接收
    print("请在服务器端发送信息！")
    recv_data = tcp_socket.recv(1024)
    print("接收到的数据为:%s" % recv_data.decode("utf-8"))

    # 4.关闭套接字
    tcp_socket.close()





if __name__ == "__main__":
    main()
