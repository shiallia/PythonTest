import requests
import logging
import time
import datetime


logger = logging.getLogger("日志")
logger.setLevel(logging.DEBUG)

#输出到屏幕
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
#输出到文件
fh = logging.FileHandler("log2.log", encoding="UTF-8")
fh.setLevel(logging.DEBUG)
#设置日志格式
fomatter = logging.Formatter('%(asctime)s:   %(message)s')
ch.setFormatter(fomatter)
fh.setFormatter(fomatter)
logger.addHandler(ch)
logger.addHandler(fh)

url1 = 'https://125.46.36.84/api/rest/external/v1/create_meeting?enterprise_id=3e816492058911e7a31d000c29971af5&meeting_name=zftest&start_time=1500645105443&end_time=1500688305443&max_participant=50&require_password=false&password=&meetin'
https_error_num = 0
https_success_num = 0

while(1):
    try:
        start_time = datetime.datetime.now()
        r = requests.get(url=url1, verify=False)    # 最基本的GET请求,忽略https验证
        end_time = datetime.datetime.now()
        https_success_num = https_success_num + 1
        logger.info(str(r.status_code) + "  " + r.text)
        logger.info('成功总数：' + str(https_success_num) + " 耗时:" + str((end_time - start_time)))
    except Exception as e:
        https_error_num = https_error_num + 1
        logger.error(e)
        logger.error("连不上啦！出错总数：" + str(https_error_num))
    finally:
        time.sleep(1)




