from socket import *  # 是的，这是一个不好的写法



def echo_client(ip , port):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.connect((ip, port))
    tempstr = input("请输入要发送的信息")
    tempstr = tempstr + '\r\n'
    sock.send(tempstr.encode(encoding="utf-8"))
    #sock.send(tempstr)
    #print(sock.recv(1024).decode(encoding='utf-8'))
    sock.close()

if __name__ == '__main__':
    echo_client('127.0.0.1', 9999)

