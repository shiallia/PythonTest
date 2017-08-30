import requests
import logging
import requests
import logging
import time
import datetime
import threading



url1 = 'http://10.254.202.36:81/1.html'
#url1 = 'https://www.baidu.com'
https_error_num = 0
https_success_num = 0

def test_xc():
    while(1):
        try:
            start_time = datetime.datetime.now()
            r = requests.get(url=url1, verify=False)    # 最基本的GET请求,忽略https验证
            end_time = datetime.datetime.now()
            #https_success_num = https_success_num + 1
            mutex.acquire()
            print(str(r.status_code) + "  " + r.text)
            mutex.release()
            #print('成功总数：' + " 耗时:" + str((end_time - start_time)))
        except Exception as e:
            #https_error_num = https_error_num + 1
            mutex.acquire()
            print(e)
            print("连不上啦！")
            mutex.release()
        finally:
            time.sleep(1)

mutex = threading.Lock()  # 创建锁
for i in range(10):
    t = threading.Thread(target=test_xc)
    t.start()











