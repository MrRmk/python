# coding=utf-8
# OS模块对文件和目录操作

import os

#创建imooc1.txt文件，以读写方式打开
fd = os.open("imooc1.txt", os.O_CREAT | os.O_RDWR)
'''
1、str通过encode()方法可以编码为指定的bytes
2、反过来，如果我们从网络或磁盘上读取了字节流，
那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：
'''
#写一句话到文件imooc1.txt中
n = os.write(fd, 'imooc1'.encode())
#文件指针复位为0
l = os.lseek(fd, 0, os.SEEK_SET)
str1 = os.read(fd, 7)
print("str1=",str1)
os.close(fd)

# 2、判断文件权限
print("imooc1.txt的文件权限是否存在：",os.access('imooc1.txt', os.F_OK))  #True
print("imooc1.txt的文件权限是否可读：",os.access('imooc1.txt', os.R_OK))  #True
print("imooc1.txt的文件权限是否可写：",os.access('imooc1.txt', os.W_OK))  #True
print("imooc1.txt的文件权限是否可执行：",os.access('imooc1.txt', os.X_OK))#True

# 3、文件
# 文件列表
print("当前目录下所有文件列表：",os.listdir('./'))
# 修改文件名 2.txt --> 3.txt
# os.rename('2.txt', '3.txt')
# 根据文件名删除文件
# os.remove('3.txt')

# 4、目录
# 创建目录
# os.mkdir('test1')   # 创建test1目录
# 创建多级目录
# os.makedirs('test2/test3/test4')
# 删除多级目录
# os.removedirs('test2/test3/test4')
# 删除目录（目录必须为空目录）
# os.rmdir('test1')

# 5、os.path模块方法介绍
# exists(path) 当前路径是否存在
print("当前目录下文件imooc.txt是否存在：",os.path.exists('./imooc.txt'))
print("当前目录下文件imooc2.txt是否存在：",os.path.exists('./imooc2.txt'))
# isdir(s) 是否是一个目录
print("当前是否是一个目录：", os.path.isdir('./'))
# isfile(path) 是否是一个文件
print("当前是否是一个文件：", os.path.isfile('imooc.txt'))
# getsize(filename) 返回文件大小
print("当前文件大小：", os.path.getsize('imooc.txt'))
# dirname(p) 返回路径的目录
print("返回路径的目录：", os.path.dirname('./imooc.txt'))
# basename(p) 返回路径的文件名
print("返回路径的文件名：", os.path.basename('./imooc.txt'))