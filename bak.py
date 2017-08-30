#!/usr/bin/env python3.5
# -*- coding:utf8 -*-
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
# 解决 访问ssl网站证书的问题
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context
class aliyunclient:
    def __init__(self):
        self.access_id = '阿里云access_id'
        self.access_secret ='阿里云secret'
        #监控获取ECS URL
        self.url = 'https://ecs.aliyuncs.com'
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
            'Format' : 'JSON',
            'Version' : '2014-05-26',
            'AccessKeyId' : self.access_id,
            'SignatureVersion' : '1.0',
            'SignatureMethod' : 'HMAC-SHA1',
            'SignatureNonce' : str(uuid.uuid1()),
            'TimeStamp' : timestamp,
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
# 继承原始类
class client(aliyunclient):
    def __init__(self,InstanceIds):
        aliyunclient.__init__(self)
        self.InstanceIds = InstanceIds
        # ECS 区域
        self.RegionId = "cn-shanghai"
    # 时间UTC转换
    def timestrip(self):
        UTCC = datetime.datetime.utcnow()
        utcbefore5 = UTCC - datetime.timedelta(minutes =5)
        Endtime = datetime.datetime.strftime(UTCC, "%Y-%m-%dT%H:%M:%SZ")
        StartTime = datetime.datetime.strftime(utcbefore5, "%Y-%m-%dT%H:%M:%SZ")
        return (StartTime,Endtime)
    def DescribeInstanceMonitorData(self):
        '''
        构造实例监控序列函数
        '''
        self.tt = self.timestrip()
        action_dict ={"StartTime":self.tt[0],"Endtime":self.tt[1],"Action":"DescribeInstanceMonitorData","RegionId":self.RegionId,"InstanceId":self.InstanceId}
        return action_dict
    def DescribeInstances(self):
        '''
        构建实例配置查询函数
        '''
        action_dict = {"Action":"DescribeInstances","RegionId":self.RegionId,"InstanceIds":self.InstanceIds}
        return action_dict
    def alis_main(self):
        res = self.do_action(self.DescribeInstances())
        listarry = len(res["Instances"]["Instance"])
        a = {}
        cpu = 0
        InternetBandwidth = 0
        instanlist = {"data":a}
        # 调用所有符合条件的实例配置数据
        for i in range(0,listarry):
            self.InstanceId = res["Instances"]["Instance"][i]["InstanceId"]
            BandwidthOUT = res["Instances"]["Instance"][i]["InternetMaxBandwidthOut"]
            # 调用计算该实例的监控数据
            monitordata = self.do_action(self.DescribeInstanceMonitorData())
            data = monitordata["MonitorData"]["InstanceMonitorData"]
            for i in range(0,len(data)):
                cpu += data[i]["CPU"]
                InternetBandwidth += data[i]["InternetBandwidth"]
            # 对该实例数据生成字典
            arry = {"BandwidthOUT":BandwidthOUT,"cpu":cpu/len(data),"InternetBandwidth":InternetBandwidth/len(data)}
            # 将新数据重构到原字典数据
            a.setdefault(self.InstanceId,arry)
        return instanlist
if __name__ == "__main__":
    # 传实例ID 列表进去
    clt= client(["i-11cy8adf2x"])
    res = clt.alis_main()
    print(res)

# 获取的结果如下：
{'data': {'i-11cy8adf2x': {'InternetBandwidth': 0.0, 'cpu': 4.0, 'BandwidthOUT': 4}}}
# 解释 获取所有实例的 当前配置的带宽值 当前占用的CPU% 当前占用的出口带宽 kbps