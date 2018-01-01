import threading
import time


def test_xc():
    mutex11.acquire()
    f = open("test.txt", "a")
    f.write("test_dxc" + '\n')
    time.sleep(1)
    f.close()
    mutex11.release()


if __name__ == '__main__':
    mutex11 = threading.Lock()  # 创建锁
    for i in range(10):
        t = threading.Thread(target=test_xc)
        t.start()

