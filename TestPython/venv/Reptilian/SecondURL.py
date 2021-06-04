# -*- coding: utf-8 -*-
print ("————————————— Python开发简单爬虫 ————————————————");
print ("————————————— 五、python爬虫urllib2下载器网页的三种方法（2） ————————————————");

import urllib.request
import urllib

# 1、网址url  http://www.baidu.com    http://localhost:8080/mobile/plugin/Advertisement.jsp
url = 'http://www.baidu.com'

# 添加数据
# word = {"wd": "豆瓣"}
# # 将请求参数转换成url编码格式（字符串）
# word = urllib.parse.urlencode(word)
# url = url + "/s?" + word

# 2、创建request请求对象
request = urllib.request.Request(url)

# 3、发送请求获取结果
response = urllib.request.urlopen(request)
htmldata = response.read()

# 4、设置编码方式
htmldata = htmldata.decode('utf-8')

# 5、打印结果
print (htmldata)

# 6、打印爬去网页的各类信息
print ("response的类型:",type(response))
print ("请求的url:",response.geturl())
print ("响应的信息:",response.info())
print ("状态码:",response.getcode())
print ("长度：",len(htmldata))

# 7、爬取数据保存到文件
fileOb = open('baidu.html','w',encoding='utf-8')     #打开一个文件，没有就新建一个
#fileOb = open('douban.html','w',encoding='utf-8')     #打开一个文件，没有就新建一个
fileOb.write(htmldata)
fileOb.close()
# 在windows下面，新文件的默认编码是gbk，这样的话，python解释器会用gbk编码去解析我们的网络数据流txt，
# 然而txt此时已经是decode过的unicode编码，这样的话就会导致解析不了，出现上述问题。
# 设置encoding='utf-8'，打开文件时就按照utf-8格式编码，则顺利运行
