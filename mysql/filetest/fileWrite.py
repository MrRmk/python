# coding=utf-8

# 文件写入
"""
0、以写方式打开文件，创建imooc文件
"""
# f = open("imooc.txt", 'w')
# f.write("test write")
# f.close()

# f = open("imooc.txt", 'w')
# f.writelines("123456 wirte")
# f.writelines(('1','2','3'))
# f.writelines(['1','2','3'])
# f.close()

f = open("imooc.txt", 'w')
f.write("1111111")
f.flush()
f.close()