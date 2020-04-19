from socket import *

def main():
    # 1.创建套间字
    udp_socket  = socket(AF_INET,SOCK_DGRAM)

    # 2.绑定一个本地信息
    localadd = ("",7788)
    udp_socket.bind(localadd)
    

    # 3.接收数据
    recv_data = udp_socket.recvfrom(1024) # 接收最大值为1024

    # 4.打印接收到的数据
    print(recv_data)
    # 5.关闭套间字
    udp_socket.close()

if __name__ == "__main__":
    main()
