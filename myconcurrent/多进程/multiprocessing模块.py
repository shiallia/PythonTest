"""
这个程序演示了最简单的多进程
在windows资源管理器里面可以看见4个python进程
1个不怎么占cpu的主进程和3个占用一颗核心的子进程
"""
import multiprocessing

def deadloop():
    print(f"进程名字：{multiprocessing.current_process().name}")
    while True:
        pass

def test():
    print("test")
    #raise(IOError)
    return -5

if __name__ == '__main__':
    t1 = multiprocessing.Process(target=deadloop)
    t2 = multiprocessing.Process(target=deadloop)
    t3 = multiprocessing.Process(target=deadloop)
    t4 = multiprocessing.Process(target=test)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t4.join()
    print(t4.exitcode)
