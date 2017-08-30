from socket import *
import threading
import queue
from concurrent.futures import ProcessPoolExecutor, as_completed,ThreadPoolExecutor
import time

q = queue.Queue()

port_List = list(range(300))
ip = '123.57.143.114'

def portScanner(port):
    global openNum
    try:
        s = socket(AF_INET,SOCK_STREAM)
        s.connect((ip,port))
        q.put(port)
        print('[+] %d open' % port)
        s.close()
    except:
        pass

def main():
    setdefaulttimeout(1)
    start = time.time()
    with ProcessPoolExecutor(max_workers=8) as executor:
       executor.map(portScanner, port_List)
    print('COST: {}'.format(time.time() - start))

    print('[*] The scan is complete!')
    #print('[*] A total of %d open port ' % (openNum))

    while not q.empty():
        print(q.get())

if __name__ == '__main__':
    main()