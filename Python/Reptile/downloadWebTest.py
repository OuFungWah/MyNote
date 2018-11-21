#!/usr/bin/python3
#! -*- coding: UTF-8 -*-

import urllib2
import cookielib
import re
from bs4 import BeautifulSoup

url = "https://www.bilibili.com"
reponse1 = urllib2.urlopen(url)
print("第一种方法")
print(reponse1.getcode())
print(reponse1.read())

url = "https://www.baidu.com"
request = urllib2.Request(url)
print("第二种方法")
# 模拟 Mozilla 进行爬虫
reponse2 = urllib2.urlopen(request)
print(reponse2.getcode())
print(reponse2.read())

url = "http://www.crazywah.com"
cookie = cookielib.CookieJar()
# 加入 urllib2 处理 Cookie 的能力
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
urllib2.install_opener(opener)
reponse3 = urllib2.urlopen(url)
print("第三种方法")
print(reponse3.getcode())
html_doc = reponse3.read()
print(html_doc)
print(cookie)

soup = BeautifulSoup(html_doc,"html.parser",from_encoding="utf-8")
links = soup.find_all('a')
print("所有链接")
for link in links:
    print(link.name)
    print(link['href'])
