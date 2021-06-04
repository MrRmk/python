# coding=utf-8
'''
自定义异常类
'''
class FileError(IOError):
    pass
try:
    raise FileError("test FileError")
except FileError as e:
    print("Error:",e)