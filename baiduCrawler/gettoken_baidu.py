#coding=utf-8
import requests
import re
#token识实在主页中加载
session = requests.Session()
response = session.get("http://fanyi.baidu.com/")
token = re.findall("token: ('.*'),",response.content.decode())[0]
print(token)