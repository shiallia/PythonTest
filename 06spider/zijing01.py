import requests
import logging
import threading
import time
import datetime


mcuHost = 'https://meeting.hn.cu.ex.sllhtv.com'
mcuHost2 = 'https://meeting.hn.cu.sllhtv.com'

testUrl = f'{mcuHost}/api/v3/meet/checkJoin.shtml'

par = {'joinAccount' : '1011',
       'joinPwd' : '111111',
       'participantName' : '张帆测试api'}

res = requests.post(testUrl, verify=False)
print(res.text)

