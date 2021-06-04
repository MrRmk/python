# coding=utf-8
'''
3.3、python正则表达式语法（三）
1、边界匹配
2、分组匹配
'''
import re

'''
1、边界匹配
'''
print('---------------1、边界匹配-------------------------')
# 以^ 和 $ 匹配字符串开头和结尾
ma = re.match(r'[\w]{4,10}@163.com', 'imooc@163.com')
print(ma.group())
ma = re.match(r'[\w]{4,10}@163.com', 'imooc@163.comabc')
print(ma)
if ma:
    print(ma.group())
ma = re.match(r'^[\w]{4,10}@163.com$', 'imooc@163.comabc')
print(ma)
if ma:
    print(ma.group())

# 指定以imooc开头的字符串
ma = re.match(r'\Aimooc[\w]*', 'imoocpython')
print(ma)
if ma:
    print(ma.group())
ma = re.match(r'\Aimooc[\w]*', 'iimoocpython')
print(ma)

'''
2、分组匹配
'''
print('---------------2、分组匹配-------------------------')
ma = re.match(r'abc|d', 'abc')
print(ma.group())
ma = re.match(r'abc|d', 'd')
print(ma.group())

# 匹配0到100之间任意一个数字组成的字符串
ma = re.match(r'[1-9]?\d$|100', '100')
print(ma.group())

# 匹配网易邮箱
ma = re.match(r'[\w]{4,6}@(163|126).com', 'imooc@163.com')
print(ma.group())
ma = re.match(r'[\w]{4,6}@(163|126).com', 'imooc@126.com')
print(ma.group())

ma = re.match(r'<[\w]+>', '<book>')
print(ma.group())
ma = re.match(r'<([\w]+>)\1', '<book>book>')
print(ma.group())
ma = re.match(r'<([\w]+>)[\w]+</\1', '<book>python</book>')
print(ma.group())
ma = re.match(r'<(?P<mark>[\w]+>)[\w]+</(?P=mark)', '<book>python</book>')
print(ma.group())


