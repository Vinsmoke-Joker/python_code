import socket

def main():
    # 创建一个udp套间字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # 可以使用套间字进行发送数据
    # udp_socket.sendto("hhhhh",对方的ip及port)  
    udp_socket.sendto(b"hhhhh------1------",("172.20.10.2",8080))  
    # 关闭套间字 
    udp_socket.close()
    print("-----run-------")

if __name__ == '__main__':
	main()
