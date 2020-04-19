import socket


def main():
    # 1.socket创建一个套接字
    tcp_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   
    # 2.bind绑定ip和port
    tcp_server.bind(("",7788))
    
    # 3.listen使套接字变为可以被动链接
    tcp_server.listen(128)
    print("-----1------")
    
    # 4.accept等待客户端的链接
    new_client_socket,new_client_addr = tcp_server.accept()
    print("****",new_client_socket,"***")
    print("+++",new_client_addr,"+++")
    print("----2-----")
    
    # 5.recv/send接收发送数据
    recv_data = new_client_socket.recv(1024)
    print("接收到的数据是:",recv_data.decode("utf-8"))

    # 回送部分数据给客户端 
    send_data = new_client_socket.send("hhhhh".encode("utf-8"))
    
    # 6.关闭套接字
    new_client_socket.close()
    tcp_server.close()


if __name__ == "__main__":
    main()
