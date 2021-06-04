# coding=utf-8
import sys;
# 2、Python标准文件

print("sys.stdin类型：",type(sys.stdin))     # <class '_io.TextIOWrapper'>
print("sys.stdin.mode：",sys.stdin.mode)     # r只读
print("sys.stdin的文件描述符：",sys.stdin.fileno())    # 0
# a = input(":0000");

sys.stdout.write('1000')    # ==>相当于 print('1000')
print("\nsys.stdout类型：",type(sys.stdout))   # <class '_io.TextIOWrapper'>
print("sys.stdout.mode：",sys.stdout.mode)     # w只写
print("sys.stdout的文件描述符：",sys.stdout.fileno())  # 1

print("\nsys.stderr类型：",type(sys.stderr))   # <class '_io.TextIOWrapper'>
print("sys.stderr.mode：",sys.stderr.mode)     # w只写
print("sys.stderr的文件描述符：",sys.stderr.fileno())    # 2

# f = open("imooc.txt")
# f.close()
