# event_loop 事件循环：程序开启一个无限的循环，程序员会把一些函数注册到事件循环上。当满足事件发生的时候，调用相应的协程函数。
# coroutine 协程：协程对象，指一个使用async关键字定义的函数，它的调用不会立即执行函数，而是会返回一个协程对象。协程对象需要注册到事件循环，由事件循环调用。
# task 任务：一个协程对象就是一个原生可以挂起的函数，任务则是对协程进一步封装，其中包含任务的各种状态。
# future： 代表将来执行或没有执行的任务的结果。它和task上没有本质的区别
# async/await 关键字：python3.5 用于定义协程的关键字，async定义一个协程，await用于挂起阻塞的异步调用接口。
from socket import *
import time
import asyncio

port_List = list(range(1, 600))
ip = '123.57.143.114'
asyncio.Semaphore(1)
loop = asyncio.get_event_loop()


async def portScanner(host, port):
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.setblocking(False)
        # await loop.sock_connect(s, (host, port), timeout=1)
        # await loop.sock_connect(s, (host, port), timeout=2000)
        await asyncio.wait_for(loop.sock_connect(s, (host, port)), timeout=1)
        print('[+] %d open' % port)
        s.close()
    except Exception as e:
        pass
        # print(e)
        # print('[-] %d close' % port)


def hello_world():
    print('Hello World')
    loop.stop()


def main():
    start = time.time()
    # setdefaulttimeout(100)            #在nonblocing的socket里面，这个失效了
    futures = []
    for port in port_List:
        futu = loop.create_task(portScanner(ip, port))
        futures.append(futu)
    loop.run_until_complete(asyncio.wait(futures))

    print('COST: {}'.format(time.time() - start))


if __name__ == '__main__':
    main()
