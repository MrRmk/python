# coding=utf-8
'''
try_finally实例
'''
try:
    f = open('1.txt')
    print(int(f.read()))
finally:
    print("file close")
    f.close()