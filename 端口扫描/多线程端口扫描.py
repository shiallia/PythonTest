from socket import *
import threading

import time

lock = threading.Lock()
openNum = 0
threads = []

def portScanner(host,port):
    global openNum
    try:
        s = socket(AF_INET,SOCK_STREAM)
        s.connect((host,port))
        lock.acquire()
        openNum+=1
        print('[+] %d open' % port)
        lock.release()
        s.close()
    except:
        pass

def main():
    start = time.time()
    setdefaulttimeout(1)
    for p in range(1, 10000):
        t = threading.Thread(target=portScanner, args=('123.57.143.114', p))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print('[*] The scan is complete!')
    print('[*] A total of %d open port ' % (openNum))
    print('COST: {}'.format(time.time() - start))

if __name__ == '__main__':
    main()