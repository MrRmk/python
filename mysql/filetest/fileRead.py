# coding=utf-8
import io,os;

# 文件读取
"""
0、以写方式打开文件，创建imooc文件
"""
# f = open("imooc.txt", 'w')
# f.write("www.imooc.com\n")
# f.write("www.imooc.com\n")
# f.write("www.imooc.com\n")
# f.close()

"""
1、第一种读取文件方式，read()：读取文件
"""
# f = open("imooc.txt")
# print (f.read())

"""
2、第二种读取文件方式，readline();读取一行
"""
# f = open("imooc.txt")
# print (f.readline())
# print (f.readline(100))
# print (f.readline(2))
# print (f.readline(2))
# print (f.readline())

"""
3、第三种读取文件方式，readlines()：读取完文件，返回每一行所组成的列表
"""
print(io.DEFAULT_BUFFER_SIZE)  # 8192
f = open("imooc.txt")
print("文件大小：",os.path.getsize("imooc.txt"),"kb")
list_c = f.readlines(1)
print (len(list_c))  # 1行   读了缓存之后list就被占满了
print (list_c)

list_c = f.readlines(14)
print (list_c)

list_c = f.readlines(28)
print (list_c)

"""
4、使用迭代器读取文件
"""
# f = open("imooc.txt")
# iter_f = iter(f)  # 文件转换为迭代器
# lines = 0
# for line in iter_f:
#     lines += 1
# print (lines)

