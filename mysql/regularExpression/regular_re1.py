# coding=utf-8
'''
2.1、python正则表达式之re模块使用（一）
'''
import re

str1 = 'imooc python'
print(str1.find('11'))      # -1
print(str1.find('imooc'))   # 0
print(str1.startswith('imooc'))     # True

pa = re.compile(r'imooc')   # 加r代表匹配原字符串
print("pa的类型：",type(pa))     # <class 're.Pattern'>
ma = pa.match(str1) # str1是要被匹配的字符串
print("ma=",ma)             # <re.Match object; span=(0, 5), match='imooc'>
print("ma.group=", ma.group())  # 匹配到的字符串内容-----imooc
print("ma.span",ma.span())      # 匹配字符串的索引位置-----(0, 5)
print("ma.string",ma.string)    # 被匹配的字符串会放到string中-----imooc python
print("ma.re",ma.re)            # 实例-----re.compile('imooc')

pa1 = re.compile(r'_')
ma1 = pa1.match('_value')
print("ma1.group=",ma1.group())  # _



