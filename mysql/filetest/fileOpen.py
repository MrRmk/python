# coding=utf-8


"""
1、以只读方式打开文件，文件必须存在（open("hello.py",'r')默认只读方式）
"""
# f = open("hello.py")
# print("文件类型：",type(f))
# c = f.read()
# f.close()
# print("文件内容如下：\n",c)
# f.write("test")     #报错io.UnsupportedOperation: not writable，因为文件打开的方式不支持写


"""
2.1、以写方式打开文件，文件不存在则创建文件
"""
# f = open("1.txt",'w')
# f.write("test write")
# f.close()

"""
2.2、以写方式打开文件，文件存在则清空文件内容
"""
# f = open("1.txt", 'w')
# f.close()

"""
3、以追加方式打开文件，文件不存在则创建文件
"""
# f = open("hello.py", 'a')
# f.write("print ('write test')")
# f.close()

"""
4.1、以读写(r+/w+)方式打开文件，r+
"""
# f = open("hello.py", 'r+')
# f.write("test r+")
# f.close()

"""
4.2、以读写(r+/w+)方式打开文件，w+
"""
f = open("hello.py", 'w+')
# f.read()
f.write("test w+ write")
f.close()

"""
5、以追加和读写方式打开文件，
"""