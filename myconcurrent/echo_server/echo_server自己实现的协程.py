from socket import *

from myconcurrent.echo_server import async_yield

loop = async_yield.Loop()


async def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    sock.setblocking(False)  # 设置非阻塞模式
    while True:
        client, addr = await loop.sock_accept(sock)
        print("connect from ", addr)
        loop.create_task(echo_handler(client))


async def echo_handler(client):
    with client:
        while True:
            data = await loop.sock_recv(client, 10000)
            if not data:
                break
            await loop.sock_sendall(client, str.encode("Got: ") + data)
    print("connection closed")

loop.create_task(echo_server(('', 25000)))
loop.run_forever()