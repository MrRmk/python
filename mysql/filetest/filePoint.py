# coding=utf-8
import os;
# 文件指针

# 以读写方式打开文件
f = open("imooc.txt", 'r+')         # 文件内容是：1234567
print("当前文件的偏移：",f.tell())  # 0
# f.write("1234567")
# print("当前文件的偏移：",f.tell())
f.read(3)
print("当前文件的偏移：",f.tell())  # 3
f.seek(0, os.SEEK_SET)
print("当前文件的偏移：",f.tell())  # 0
f.close()

# 偏移超过文件位置会报错