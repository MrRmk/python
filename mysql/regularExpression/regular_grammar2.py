# coding=utf-8
'''
3.2、python正则表达式语法（二）
'''
import re

# 匹配首字母大写的字符串
# [A-Z]：表示首字母大写
# [a-z]*：表示0个或多个a-z其中的字母
ma = re.match(r'[A-Z][a-z]*', 'A')
print(ma.group())               # A
ma = re.match(r'[A-Z][a-z]*', 'Ahbdkasdhka')
print(ma.group())               # Ahbdkasdhka

ma = re.match(r'[_a-zA-Z]+[_\w]*', '_Asa')
print(ma)                       
if ma:
    print(ma.group())

# 匹配0到99之间的数
ma = re.match(r'[_1-9]?[0-9]', '99')
print(ma)
if ma:
    print(ma.group())

ma = re.match(r'[_1-9]?[0-9]', '09')
print(ma)
if ma:
    print(ma.group())

ma = re.match(r'[a-zA-Z0-9]{6}', 'abc123')
print(ma)
if ma:
    print(ma.group())

# 匹配6位到10位的网易邮箱
ma = re.match(r'[a-zA-Z0-9]{6,10}@163.com', 'abc123456@163.com')
print(ma)
if ma:
    print(ma.group())

# 非贪婪算法 尽可能的少匹配  *? / +? / ??
ma = re.match(r'[0-9][a-z]*', '1bc')
print(ma)
if ma:
    print(ma.group())   # 1bc
ma = re.match(r'[0-9][a-z]*?', '1bc')
print(ma)
if ma:
    print(ma.group())   # 1
ma = re.match(r'[0-9][a-z]+?', '1bc')
print(ma)
if ma:
    print(ma.group())   # 1b
ma = re.match(r'[0-9][a-z]??', '1bc')
print(ma)
if ma:
    print(ma.group())   # 1