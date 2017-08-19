try: import httplib
except ImportError:
    import http.client as httplib
import sys, datetime
import urllib
import urllib.request
import urllib.error
import urllib.parse
import time
import json
import base64
import hmac,ssl
import uuid
from hashlib import sha1

class aliyunclient:
    def __init__(self):
        self.access_id = 'w1jPPOxPEtB8Q44g'
        self.access_secret ='qjf8b2uvltKEDsVuFMd9oLDgtkkw05'
        #监控获取ECS URL
        self.url = 'alidns.aliyuncs.com'
    # #签名
    def sign(self,accessKeySecret, parameters):
        sortedParameters = sorted(parameters.items(), key=lambda parameters: parameters[0])
        canonicalizedQueryString = ''
        for (k,v) in sortedParameters:
            canonicalizedQueryString += '&' + self.percent_encode(k) + '=' + self.percent_encode(v)
        stringToSign = 'GET&%2F&' + self.percent_encode(canonicalizedQueryString[1:])  # 使用get请求方法
        bs = accessKeySecret +'&'
        bs = bytes(bs,encoding='utf8')
        stringToSign = bytes(stringToSign,encoding='utf8')
        h = hmac.new(bs, stringToSign, sha1)
        # 进行编码
        signature = base64.b64encode(h.digest()).strip()
        return signature
    def percent_encode(self,encodeStr):
        encodeStr = str(encodeStr)
        res = urllib.request.quote(encodeStr)
        res = res.replace('+', '%20')
        res = res.replace('*', '%2A')
        res = res.replace('%7E', '~')
        return res
    # 构建除共公参数外的所有URL
    def make_url(self,params):
        timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        parameters = {
            'Format': 'JSON',
            'Version': '2014-05-26',
            'AccessKeyId': self.access_id,
            'SignatureVersion': '1.0',
            'SignatureMethod': 'HMAC-SHA1',
            'SignatureNonce': str(uuid.uuid1()),
            'TimeStamp': timestamp,
        }
        for key in params.keys():
            parameters[key] = params[key]
        signature = self.sign(self.access_secret,parameters)
        parameters['Signature'] = signature
        url = self.url + "/?" + urllib.parse.urlencode(parameters)
        return url
    def do_action(self,params):
        url = self.make_url(params)
        # print(url)
        request = urllib.request.Request(url)
        try:
            conn = urllib.request.urlopen(request)
            response = conn.read().decode()
        except urllib.error.HTTPError as e:
            print(e.read().strip())
            raise SystemExit(e)
        try:
            res = json.loads(response)
        except ValueError as e:
            raise SystemExit(e)
        return res

if __name__ == '__main__':
    testclient = aliyunclient()
    parm = {
        "Action": "UpdateDomainRecord",
        "RecordId": "",
        "RR": "www.gozhangfango.xyz",
        "Type": "A",
        "Value": "123.57.70.225",





    }
    testclient.do_action()



