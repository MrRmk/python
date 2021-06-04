# coding=utf-8
'''
try_except_else_finally 实例
'''
try:
    f = open('1.txt')
    line = f.read(2)
    num = int(line)
    print("read num=%d" % num)
except IOError as e:
    print("catch IOError:",e)
except ValueError as e:
    print("catch ValueError:", e)
else:
    print("No Error")
finally:
    try:
        print("close file")
        f.close()
    except NameError as e:
        print("catch NameError:", e)