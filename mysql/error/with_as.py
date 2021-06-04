# coding=utf-8
'''
with_as 实例
'''
import os
try:
    f = open('1.txt')
    print("in try f.read():", f.read(2))
    f.seek(-5, os.SEEK_SET)
except IOError as e:
    print("catch IOError:",e)
except ValueError as e:
    print("catch ValueError:", e)
finally:
    f.close()
print("try-finally:", f.closed)

'''
with不发生错误的话会将文件关闭
发生错误的话不会将文件关闭，需要处理异常
'''
try:
    with open("1.txt") as f1:
        print("in with f1.read:", f1.read())
        f.seek(-5, os.SEEK_SET)
except ValueError as e:
    print("in with catch ValueError:", e)
    print("with:", f1.closed)