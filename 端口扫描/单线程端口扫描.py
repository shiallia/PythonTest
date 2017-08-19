from socket import *
import time

def portScanner(host,port):
    try:
        s = socket(AF_INET,SOCK_STREAM)
        s.connect((host,port))
        print('[+] %d open' % port)
        s.close()
    except:
        print('[-] %d close' % port)

def main():
    setdefaulttimeout(1)
    start = time.time()
    for p in range(50):
        portScanner('123.57.143.114', p)
    print('COST: {}'.format(time.time() - start))

if __name__ == '__main__':
    main()