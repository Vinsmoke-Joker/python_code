import socket

# 1.创建套接字
udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 2.绑定信息
local_addr = ("",7788)
udp_socket.bind(local_addr)

# 3.发送/接收数据
send_data = udp_socket.sendto(("xxxxxx".encode("utf_8")),("192.168.158.128",7788))
recv_data = recvfrom(1024)
recv_data = udp_socket.recvfrom()

# 4.打印接收到的数据
# recv_data[1]为ip tuple类型，recv_data[0]为接收内容需要解码为gbk
print("[%s]:%s"%(str(recv_data[1]),recv_data[0].decode("gbk")))

# 5.关闭套接字
udp_socket.close()