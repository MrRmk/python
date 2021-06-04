# coding=utf-8

import sys,os

print('The command line argument are:')
for i in sys.argv:
    #当前文件路径
    print(i)

print('\n\nThe python path is',sys.path,'\n')

#查看当前目录
print('\n',os.getcwd(),'\n')


