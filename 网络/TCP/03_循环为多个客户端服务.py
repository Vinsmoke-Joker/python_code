import socket


def main():

    # 1.创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    # 2.绑定信息
    tcp_server_socket.bind(("",7788))
    
    # 3.listen套接字变为被动链接
    tcp_server_socket.listen(128)
    
    while True:
        print("等待一个新的客户端连入......") 
        # 4.accept 等待客户端连入
        new_client_socket,new_client_addr = tcp_server_socket.accept()
        print("一个新的客户端已经到来 %s" % str(new_client_addr))
        # 5.发送/接收数据
        recv_data = new_client_socket.recv(1024)
        print("客户端发送过来的请求是:%s" % recv_data.decode("utf-8"))

        send_data = new_client_socket.send("hhhhh".encode("utf-8"))

        # 6.关闭套接字
        new_client_socket.close()
        print("服务完毕.....")
    
    tcp_server_socket.close()


if __name__ == "__main__":
    main()

