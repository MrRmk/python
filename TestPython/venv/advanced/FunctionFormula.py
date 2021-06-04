# -*- coding: utf-8 -*-

print ("————————————— Python进阶学习————————————————");
print ("————————————— 一、函数式编程————————————————");

print ("————————————— 1、高阶函数————————————————");
#   能接收函数作为参数的函数就是高阶函数
import math
def add(x,y,f):
    return f(x) + f(y)

print (add(-4, 9, abs))
print (add(25, 9, math.sqrt))

print ("————————————— 2、python中map()函数————————————————");
'''
假设用户输入的英文名字不规范，没有按照首字母大写，后续字母小写的规则，请利用map()函数，把一个list（包含若干不规范的英文名字）变成一个包含规范英文名字的list：
输入：['adam', 'LISA', 'barT']
输出：['Adam', 'Lisa', 'Bart']
'''
def format_name(s):
    return s[0:1].upper() + s[1:].lower()

print ( list(map(format_name, ['adam', 'LISA', 'barT'])) );

print ("————————————— 3、python中reduce()函数————————————————");
'''
Python内置了求和函数sum()，但没有求积的函数，请利用recude()来求积：
输入：[2, 4, 5, 7, 12]
输出：2*4*5*7*12的结果
'''
from functools import reduce
def prod(x,y):
    return x * y

print ( reduce(prod, [2, 4, 5, 7, 12]) );

print ("————————————— 4、python中filter()函数 ————————————————");
'''
请利用filter()过滤出1~100中平方根是整数的数，即结果应该是：
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''
import math
def is_sqr(x):
    return math.sqrt(x) % 1 == 0

print ( list(filter(is_sqr, list(range(1,101)))) );

print ("————————————— 5、python中自定义排序函数 ————————————————");
'''
对字符串排序时，有时候忽略大小写排序更符合习惯。
请利用sorted()高阶函数，实现忽略大小写排序的算法。
输入：['bob', 'about', 'Zoo', 'Credit']
输出：['about', 'bob', 'Credit', 'Zoo']
'''

def cmp_ignore_case(x):
    return x.upper()
print ( sorted(['bob', 'about', 'Zoo', 'Credit'], key = cmp_ignore_case) );

print ( sorted(['bob', 'about', 'Zoo', 'Credit'], key = lambda x: x.upper()) );

print ("————————————— 6、python中返回函数 ————————————————");
'''
请编写一个函数calc_prod(lst)，它接收一个list，返回一个函数，返回函数可以计算参数的乘积。
'''
def calc_prod(lst):
    def mult_list():
        sum = 1
        for x in lst:
            sum = sum * x
        return sum
    return mult_list
f = calc_prod([1,2,3,4])
print ( f() );

print ("————————————— 7、python中闭包 ————————————————");
'''
返回闭包不能引用循环变量，请改写count()函数，让它正确返回能计算1x1、2x2、3x3的函数。
'''
def count():
    fs = []
    for i in list(range(1,4)):
        def f(j):
            def g():
                return j*j
            return g
        r = f(i)
        fs.append(r)
    return fs

f1, f2, f3 = count()
print ( f1(), f2(), f3() )

print ("————————————— 8、python中匿名函数 ————————————————");
'''
利用匿名函数简化以下代码：
def is_not_empty(s):
    return s and len(s.strip()) > 0
filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])
'''
print ( list(filter(lambda s: s and len(s.strip()) > 0 , ['test', None, '', 'str', '  ', 'END'] )) )

print ("————————————— 9、python中编写无参数decorator ————————————————");
'''
请编写一个@performance，它可以打印出函数调用的时间。
'''
import time

def performance(f):
    def fn(*args, **kw):
        t1 = time.time()
        r = f(*args, **kw)
        t2 = time.time()
        print ('call %s() in %fs' % (f.__name__, (t2-t1)))
        return r
    return fn

@performance
def factorial(n):
    return reduce(lambda x,y: x*y, list(range(1, n+1)))

print (factorial(10))

print ("————————————— 10、python中编写带参数decorator ————————————————");
'''
上一节的@performance只能打印秒，请给 @performace 增加一个参数，允许传入's'或'ms'：
@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
'''
import time

def performance(unit):
    def performance_decor(f):
        def fn(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit=='ms' else (t2 - t1)
            print ('call %s() in %f %s' % (f.__name__, t, unit))
            return r
        return fn
    return performance_decor

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, list(range(1, n+1)))

print (factorial(10))

print ("————————————— 11、python中完善decorator ————————————————");
'''
请思考带参数的@decorator，@functools.wraps应该放置在哪：
def performance(unit):
    def perf_decorator(f):
        def wrapper(*args, **kw):
            ???
        return wrapper
    return perf_decorator
'''
import time, functools

def performance(unit):
    def perf_decorator(f):
        @functools.wraps(f)
        def fn(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit == 'ms' else (t2 - t1)
            print ('call %s in %f%s' % (f.__name__, t, unit))
            return r
        return fn
    return perf_decorator

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print (factorial.__name__)

print ("————————————— 12、python中偏函数 ————————————————");
'''
我们在sorted这个高阶函数中传入自定义排序函数就可以实现忽略大小写排序。
请用functools.partial把这个复杂调用变成一个简单的函数：
sorted_ignore_case(iterable)
'''
import functools
sorted_ignore_case = functools.partial(sorted, key=lambda x: x.upper())
print (sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit']))