# echo.py
from socket import *  # 是的，这是一个不好的写法


def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    while True:
        client, addr = sock.accept()
        print("connect from ", addr)
        echo_handler(client)


def echo_handler(client):
    while True:
        data = client.recv(10000)
        if not data:
            break
        client.send(str.encode("Got: ") + data)
    print("connection closed.")

if __name__ == '__main__':
    echo_server(('', 25000))
