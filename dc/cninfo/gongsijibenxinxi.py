#-*- coding: UTF-8 -*-

import json
import urllib
import requests
import datetime

####用于获取token
def gettoken(client_id,client_secret):
    url='http://webapi.cninfo.com.cn/api-cloud-platform/oauth2/token'
    post_data="grant_type=client_credentials&client_id=%s&client_secret=%s"%(client_id,client_secret)
    post_data={"grant_type":"client_credentials",
               "client_id":client_id,
               "client_secret":client_secret
               }
    req = requests.post(url, data=post_data)
    tokendic = json.loads(req.text)
    return tokendic['access_token']

####用于解析接口返回内容
def getPage(url):
    response = urllib.request.urlopen(url)
    return response.read().decode('utf-8')

token = gettoken('xxxxxxxxx','xxxxxxxxx') ##请在平台注册后并填入个人中心-我的凭证中的Access Key，Access Secret
url = 'http://webapi.cninfo.com.cn/api/stock/p_stock2100?scode=000002&access_token='+token
print(url)
result = json.loads(getPage(url))
for i in range(len(result['records'])):
    print (result['records'][i])