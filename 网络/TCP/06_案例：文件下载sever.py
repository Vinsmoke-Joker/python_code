import socket

def send_file_2_client(tcp_client_socket,tcp_client_addr):
    # 1.接收客户端发送来的要下载的文件名
    file_name = tcp_client_socket.recv(1024).decode("utf-8")
    print("客户端【%s】要下载的文件是:%s" % (str(tcp_client_addr),file_name))
    # 2.打开文件读取数据
    file_content = None  # 用于判断是否文件为空
    # with open一般用于写文件，若文件不存在会新建文件，因此不会抛出异常
    # 若文件不存在，with open会抛出异常，因此读文件时，采取try...except...
    try:
        f = open(file_name,"rb")  # 打开
        file_content = f.read()  # 打开成功后读取
        f.close()
    except Exception as ref:
        print("没有要下载的文件%s" % file_name)
    # 文件不为空，发送
    if file_content:
        # 3.服务器发送回执信息给客户端
        # file_content以二进制rb读入，因此不需要encode
        send_data = tcp_client_socket.send(file_content)

def main():
    # 1.创建套接字
    tcp_sever_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 2.绑定本地信息
    tcp_sever_socket.bind(("",7788))
    # 3.listen让套接字默认变为被动
    tcp_sever_socket.listen(128)
    while True:
        # 4.等待客户端连入
        tcp_client_socket,tcp_client_addr = tcp_sever_socket.accept()
        # 5.调用发送文件函数，完成为客户端服务
        send_file_2_client(tcp_client_socket,tcp_client_addr)
        # 6.关闭套接字
        tcp_client_socket.close()
    tcp_sever_socket.close()


if __name__ == "__main__":
    main()
