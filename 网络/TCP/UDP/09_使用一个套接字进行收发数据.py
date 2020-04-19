import socket

def main():
    # 创建一个udp套间字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # 获取对方的ip和port
    dest_ip = input("请输入对方的ip:")
    dest_port =int(input("请输入对方的port:"))
   
    # 从键盘获取数据
    send_data = input("请输入所要发送的数据:")
    # 可以使用套间字进行发送数据
    # udp_socket.sendto("hhhhh",对方的ip及port)  
    udp_socket.sendto(send_data.encode("utf-8"),(dest_ip,dest_port))
    # 接收回送数据
    recv_data = udp_socket.recvfrom(1024)
    # 打印接收到的数据
    print("[%s]:%s"%(str(recv_data[1]),recv_data[0].decode("gbk")))
    # 关闭套间字 
    udp_socket.close()
    print("-----run-------")

if __name__ == '__main__':
	main()
