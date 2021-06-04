# coding=utf-8
# 文件属性

# 1、文件属性
# f = open("imooc.txt")
# print("文件描述符：",f.fileno())       # 3
# print("文件打开权限："+f.mode)         # r
# print("文件编码格式：",f.encoding)     # cp936
# print("文件是否关闭：",f.closed)       # False
# f.close()


# 4、文件属性编码
# from idna import unicode
# import os
#
# a = unicode.encode(u'慕课', 'utf-8')
# print(a)
# f = open("imooc.txt",'wb+')
# f.write(a)
# f.seek(0, os.SEEK_SET)
# print(f.read())
# f.close()
# 执行结果：文件内容为：慕课


# 5、文件编码格式
import codecs

f = codecs.open('test.txt', 'w', 'utf-8')
print(f.encoding)
f.write("慕课")
# f.close()
