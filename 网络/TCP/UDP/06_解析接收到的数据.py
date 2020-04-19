from socket import *

def main():
    # 1.创建套间字
    udp_socket  = socket(AF_INET,SOCK_DGRAM)

    # 2.绑定一个本地信息
    localadd = ("",7788)
    udp_socket.bind(localadd)
    
    # 3.接收数据
    # recv_data 这个变量中接收到的是一个元组(接收到的数据,(发送方的ip,端口))
    recv_data = udp_socket.recvfrom(1024) # 接收最大值为1024
    recv_msg = recv_data[0]  # 接收到的数据
    send_addr = recv_data[1]  #（发送方的ip，端口）

    # 4.打印接收到的数据
    # send_addr为元组；
    # windows中编码方式为gbk,recv_msg需要调用decode("gbk")解码
    print("[%s]:%s"%(str(send_addr),recv_msg.decode("gbk"))
    # 5.关闭套间字
    udp_socket.close()
    
    

if __name__ == "__main__":
    main()
