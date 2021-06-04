# coding=utf-8
'''
4.2、python正则表达式练习
抓取网页中的图片到本地
1、抓取网页
2、获取图片地址
3、抓取图片内容并保存到本地
'''
import urllib.request
import re

'''
实例：获取 豆瓣电影 Top 250 中第一页的图片
'''
url = 'https://movie.douban.com/top250'
request = urllib.request.Request(url)
request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36')
response = urllib.request.urlopen(request)
buf = response.read()
buf = str(buf, encoding='utf-8')
# print(buf)
# 获取所有图片url地址列表
listurl = re.findall(r'http.+\.jpg', buf)
print(listurl)

i = 1
for url in listurl:
    f = open(str(i)+'.jpg', 'wb+')
    req = urllib.request.urlopen(url)
    buf = req.read()
    # buf = str(buf)
    f.write(buf)
    i += 1
