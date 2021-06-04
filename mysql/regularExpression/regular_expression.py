# coding=utf-8
'''
1.1、正则简介
正则表达式
场景1、找到imooc开头和结尾的语句
场景2、找到imooc开头和结尾的语句
场景3、匹配一个下划线和字母开头的变量名
'''
print("imooc test".startswith("imooc"))
print( "imooc test imooc".startswith("imooc") and "imooc test imooc".endswith("imooc") )
# a = '_value'
a = '1_value'
print(a and (a[0]=='_' or 'a' <= a[0] <= 'z'))