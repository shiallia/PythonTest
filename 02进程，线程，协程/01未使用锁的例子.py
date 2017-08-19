import threading
import time


def test_xc():
    f = open("test.txt", "a")
    f.write("test_dxc" + '\n')
    time.sleep(1)
    f.close()


if __name__ == '__main__':
    for i in range(10):
        t = threading.Thread(target=test_xc)
        t.start()
