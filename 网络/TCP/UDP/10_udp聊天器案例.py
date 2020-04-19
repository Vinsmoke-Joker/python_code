from socket import *


def send_msg(udp_socket):
    """发送消息"""
    # 获取发送的ip,port,内容
    dest_ip = input("请输入要发送的ip:")
    dest_port = int(input("请输入要发送的port:"))
    send_data = input("请输入要发送的内容:")
    # 发送数据
    udp_socket.sendto(send_data.encode("utf-8"),(dest_ip,dest_port))

def recv_msg(udp_socket):
    """接收消息"""
    # 接收并显示
    recv_data = udp_socket.recvfrom(1024)
    # 打印并显示
    print("[%s]:%s" % (str(recv_data[1]),recv_data[0].decode("utf-8")))

def main():
    # 创建套接字
    udp_socket = socket(AF_INET,SOCK_DGRAM)
    # 绑定信息
    local_addr = ("",7788)
    udp_socket.bind(local_addr)
    # 循环处理
    while True:
        # 选择功能
        print("="*30)
        op_num = int(input("输入所需要选择的功能:1.发送 2.接收 3.退出:"))
        if op_num == 1:
            # 发送
            send_msg(udp_socket)
        elif op_num == 2:
            # 接收
            recv_msg(udp_socket)
        elif op_num == 3:
            break
        else:
            print("输入错误，请重新输入！")


if __name__ == "__main__":
    main()
