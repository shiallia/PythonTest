'''
这个例子说明多线程必须加锁
'''
import threading

counter = 0
mutex = threading.RLock()

counter_withoutlock = 0


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

class MyThreadWithoutLock(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global counter_withoutlock
        for i in range(100000):
            counter_withoutlock += i
        for i in range(100000):
            counter_withoutlock -= i
        print("I am %s, set counter:%s" % (self.name, counter_withoutlock))


if __name__ == "__main__":
    thread_list = []
    thread_list_withoutlock = []
    for i in range(0, 10):
        my_thread = MyThread()
        thread_list.append(my_thread)
    for th in thread_list:
        th.start()
    for th in thread_list:
        th.join()

    for i in range(0, 10):
        my_thread = MyThreadWithoutLock()
        thread_list_withoutlock.append(my_thread)
    for th in thread_list_withoutlock:
        th.start()
