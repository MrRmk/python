# coding=utf-8
'''
4.1、python正则表达式之re模块方法介绍
'''
import re

'''
1、search()在一个字符串中查找匹配
'''
str1 = 'imooc videonum = 1000'
info = re.search(r'\d+', str1)
print("info1.group=", info.group())  # info1.group= 1000

str1 = 'imooc videonum = 10000'
info = re.search(r'\d+', str1)
print("info2.group=", info.group())  # info2.group= 10000

'''
2、findall()找到匹配，返回所以匹配部分的列表
'''
str2 = 'c++=100, java=90, python=80'
info = re.search(r'\d+', str2)
print("info3.group=", info.group())  # info3.group= 100
info = re.findall(r'\d+', str2)
print("info4=", info)                # info4= ['100', '90', '80']
# 把所有科目的时长加在一起， 列表解析sum 来解析info列表
print(sum([int(x) for x in info]))   # 270

'''
3、sub()将字符串中匹配正则表达式的部分替换为其他值
'''
def add1(match):
    val = match.group()
    num = int(val) + 1
    return str(num)

str3 = 'imooc videonum = 9999'
info = re.sub(r'\d+', add1, str3)
print(info)     # imooc videonum = 10000

'''
4、split()根据匹配分割字符串，返回分割字符串组成的列表
'''
str4 = 'imooc:C C++ Java Python'
print(re.split(r':| ', str4))       # ['imooc', 'C', 'C++', 'Java', 'Python']

str4 = 'imooc:C C++ Java Python,C#'
print(re.split(r':| |,', str4))       # ['imooc', 'C', 'C++', 'Java', 'Python', 'C#']

