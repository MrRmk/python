# coding=utf-8
'''
3.1、python正则表达式语法（一）
'''
import re

ma = re.match(r'a', 'a')
print(ma.group())

ma = re.match(r'a', 'b')
print(type(ma))

# . 小数点可以匹配任意字符（除了\n）
ma = re.match(r'.', 'b')
print(type(ma))
print(ma.group())

ma = re.match(r'{.}', '{0}')
print(ma.group())

ma = re.match(r'{..}', '{01}')
print(ma.group())

ma = re.match(r'{[abc]}', '{a}')
print(ma.group())

ma = re.match(r'{[a-z]}', '{a}')
print(ma.group())

ma = re.match(r'{[a-zA-Z]}', '{A}')
print(ma.group())

ma = re.match(r'{[a-zA-Z0-9]}', '{1}')
print(ma.group())

ma = re.match(r'{[\w]}', '{1}')
print(ma.group())

ma = re.match(r'{[\W]}', '{ }')
print(ma.group())

ma = re.match(r'\[[\w]\]', '[a]')
print(ma.group())

