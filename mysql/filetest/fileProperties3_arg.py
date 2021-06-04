# coding=utf-8
import sys
# 3、文件命令行参数

if __name__ == '__main__':
    print(len(sys.argv))
    for arg in sys.argv:
        print(arg)

'''
执行结果：
1
D:/python/mysql/filetest/fileProperties3_arg.py
'''