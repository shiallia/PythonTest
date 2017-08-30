import threading
import queue
import time
import random

def read(q):
    while True:
        try:
            value = q.get()
            print('Get %s from queue.' % value)
<<<<<<< HEAD
            print()
=======
>>>>>>> origin/master
            time.sleep(1)
        except Exception as e:
            print(e)

def main():
    q = queue.Queue()
    pw1 = threading.Thread(target=read, args=(q,))
    pw2 = threading.Thread(target=read, args=(q,))
    pw3 = threading.Thread(target=read, args=(q,))
    pw4 = threading.Thread(target=read, args=(q,))
    pw1.daemon = True
    pw2.daemon = True
    pw3.daemon = True
    pw4.daemon = True
    pw1.start()
    pw2.start()
    pw3.start()
    pw4.start()
    for c in [chr(ord('A')+i) for i in range(26)]:
        q.put(c)
    try:
        #q.join()
        pw1.join()
        pw2.join()
        pw3.join()
        pw4.join()
    except KeyboardInterrupt:
        print("stopped by hand")

if __name__ == '__main__':
    main()