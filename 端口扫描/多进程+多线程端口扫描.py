from socket import *
import queue
from concurrent.futures import ProcessPoolExecutor, as_completed,ThreadPoolExecutor
from multiprocessing import Process
import time

q = queue.Queue()

port_List = list(range(64000))
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
        print('[+] %d notopen' % port)


def workThread(port_List):
    setdefaulttimeout(1)
    with ThreadPoolExecutor(max_workers=500) as executor:
        executor.map(portScanner, port_List)


def main():
    setdefaulttimeout(1)
    start = time.time()
    endlist = list_of_groups(port_List, int(64000/8))
    processList = []
    for k in range(8):
        myProcess = Process(target=workThread, args=(endlist[k],))
        processList.append(myProcess)
        myProcess.start()

    for proc in processList:
        proc.join()

    print('[*] The scan is complete!')

    # while not q.empty():
    #     print(q.get())

    print('COST: {}'.format(time.time() - start))


def list_of_groups(init_list, childern_list_len):
    list_of_groups = zip(*(iter(init_list),) *childern_list_len)
    end_list = [list(i) for i in list_of_groups]
    count = len(init_list) % childern_list_len
    end_list.append(init_list[-count:]) if count !=0 else end_list
    return end_list



if __name__ == '__main__':
    main()