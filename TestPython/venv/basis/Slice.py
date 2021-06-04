# -*- coding: utf-8 -*-

print ("————————————— 六、Python之切片————————————————");
print ("\n---------------1、对list进行切片--------------------");
L = ['Adam', 'Lisa', 'Paul', 'Bart']
r = []
n = 3
for i in range(n):
    r.append(L[i])
print (r)
#   对这种经常取指定索引范围的操作，用循环十分繁琐，
#   因此，Python提供了切片（Slice）操作符，能大大简化这种操作。

'''
例题：
range()函数可以创建一个数列：
>>> range(1, 101)
[1, 2, 3, ..., 100]
请利用切片，取出：
1. 前10个数；
2. 3的倍数；
3. 不大于50的5的倍数。
'''
#   L = range(1, 101)
#   L = list(L)
L = list(range(1, 101))
print (L);
print (L[:10]);
print (L[2::3]);
print (L[4:50:5]);

print ("\n---------------2、倒序切片--------------------");
'''
例题：
利用倒序切片对 1 - 100 的数列取出：
* 最后10个数；
* 最后10个5的倍数。
'''
L = list(range(1, 101))

print (L[-10:]);
print (L[-46::5]);

print ("\n---------------3、对字符串切片--------------------");
'''
字符串有个方法 upper() 可以把字符变成大写字母：
>>> 'abc'.upper()
'ABC'
但它会把所有字母都变成大写。请设计一个函数，它接受一个字符串，然后返回一个仅首字母变成大写的字符串。
提示：利用切片操作简化字符串操作。
'''
def firstCharUpper(s):
    return s[0:1].upper() + s[1:]

print (firstCharUpper('hello'));
print (firstCharUpper('sunday'));
print (firstCharUpper('september'));