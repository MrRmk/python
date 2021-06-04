# -*- coding: utf-8 -*-
print ("————————————— 六、Python爬虫之网页解析器BeautifulSoup ————————————————");

from bs4 import BeautifulSoup   #导入网页解析器BeautifulSoup库
import re                       #导入正则表达式库

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# 1、创建BeautifulSoup对象
soup = BeautifulSoup(html_doc,                  # HTML文档字符串
                     'html.parser',             # HTML解析器
                     #from_encoding='utf-8'      # HTML文档的编码
           )

# 2、搜索节点（find_all, find）
print ('获取所有的链接')
links = soup.find_all('a')
for link in links:
    # 3、访问节点内容
    print (link.name, link['href'], link.get_text())

print ('获取Lacie的链接')
link_node = soup.find('a', href='http://example.com/lacie')
print (link_node.name, link_node['href'], link_node.get_text())

print ('正则匹配')
link_node = soup.find('a', href=re.compile(r"ill"))
print (link_node.name, link_node['href'], link_node.get_text())

print ('获取p段落文字')
link_node = soup.find('p', class_="title")
print (link_node.name, link_node.get_text())

'''
报错：
UserWarning: You provided Unicode markup but also provided a value for from_encoding. Your from_encoding will be ignored.
解决方法：
soup = BeautifulSoup(html_doc,"html.parser")
这一句中删除【from_encoding="utf-8"】
原因：
python3 缺省的编码是unicode, 再在from_encoding设置为utf8, 会被忽视掉，去掉【from_encoding="utf-8"】这一个好了
'''