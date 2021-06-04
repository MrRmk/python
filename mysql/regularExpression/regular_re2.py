# coding=utf-8
'''
2.2、python正则表达式之re模块使用（二）
'''
import re

pa = re.compile(r'imooc', re.I)   # 加r代表匹配原字符串, re.I 代表大写
print("pa=",pa)             # re.compile('imooc', re.IGNORECASE)
ma = pa.match('imooc python')         # str1是要被匹配的字符串
print("ma=",ma)             # <re.Match object; span=(0, 5), match='imooc'>
print("ma.group=", ma.group())  # 匹配到的字符串内容-----imooc

ma = pa.match('ImOoc python')
print("ma.group=",ma.group())  # ImOoc
print("ma.groups=",ma.groups())  # ()

ma = re.match(r'imooc', 'imooc python')
print("ma=",ma)             # <re.Match object; span=(0, 5), match='imooc'>
print("ma.group=", ma.group())  # 匹配到的字符串内容-----imooc
print("ma.group=",ma.group())  # ImOoc
print("ma.groups=",ma.groups())  # ()
