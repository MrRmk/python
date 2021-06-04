# -*- coding: utf-8 -*-
print ("————————————— Python开发简单爬虫 ————————————————");
print ("————————————— 五、python爬虫urllib2下载器网页的三种方法（1） ————————————————");

import urllib.request

# 1、网址url
url = 'http://www.douban.com'

# 2、直接请求  返回结果
response = urllib.request.urlopen(url)

# 3、获取状态码，如果是200表示获取成功
print ('状态码：',response.getcode())

# 4、读取内容
data = response.read()

# 5、设置编码
data = data.decode('utf-8')

# 6、打印结果
print (data)
print ("长度：",len(data))
#print (data.decode("utf-8"))