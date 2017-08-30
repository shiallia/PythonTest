'''
这个例子说明多线程必须加锁
'''
import threading

counter = 0
mutex = threading.Lock()


class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global counter, mutex
        mutex.acquire()
        for i in range(100000):
            counter += i
        for i in range(100000):
            counter -= i
        print("I am %s, set counter:%s" % (self.name, counter))
        mutex.release()


if __name__ == "__main__":
    thread_list = []
    for i in range(0, 10000):
        my_thread = MyThread()
        thread_list.append(my_thread)
    for th in thread_list:
        th.start()
