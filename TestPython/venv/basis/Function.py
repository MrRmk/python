# -*- coding: utf-8 -*-

print ("————————————— 五、Python之函数————————————————");
print ("\n---------------1、Python之调用函数--------------------");
#   sum()函数接受一个list作为参数，并返回list所有元素之和。
#   请计算 1*1 + 2*2 + 3*3 + ... + 100*100。
L = [];
x = 1
while x <= 100:
    L.append(x * x)
    x = x + 1
print (L)
print (sum(L))

print ("\n---------------2、Python之编写函数--------------------");
#   请定义一个 square_of_sum 函数，它接受一个list，
#   返回list中每个元素平方的和。
def square_of_sum(L):
    sum = 0
    for x in L:
        sum = sum + x * x
    return sum

print (square_of_sum([1, 2, 3, 4, 5]))
print (square_of_sum([-5, 0, 5, 10 ]))

print ("\n---------------3、Python函数之返回多值--------------------");
#   一元二次方程的定义是：ax² + bx + c = 0
#   请编写一个函数，返回一元二次方程的两个解。
#   注意：Python的math包提供了sqrt()函数用于计算平方根
import math
def quadratic_equation(a, b, c):
    x1 = (-b + math.sqrt(b*b - 4*a*c))/(2*a)
    x2 = (-b - math.sqrt(b*b - 4*a*c))/(2*a)
    return x1, x2

print (quadratic_equation(2, 3, 0))
print (quadratic_equation(1, -6, 5))

print ("\n---------------4、Python函数之递归函数--------------------");
'''
汉诺塔 (http://baike.baidu.com/view/191666.htm) 的移动也可以看做是递归函数。
我们对柱子编号为a, b, c，将所有圆盘从a移到c可以描述为：
如果a只有一个圆盘，可以直接移动到c；
如果a有N个圆盘，可以看成a有1个圆盘（底盘） + (N-1)个圆盘，首先需要把 (N-1) 个圆盘移动到 b，然后，将 a的最后一个圆盘移动到c，再将b的(N-1)个圆盘移动到c。
请编写一个函数，给定输入 n, a, b, c，打印出移动的步骤：
move(n, a, b, c)
例如，输入 move(2, 'A', 'B', 'C')，打印出：
A --> B
A --> C
B --> C
'''
def move(n, a, b, c):
    if n == 1:
        print (a, '-->' , c)
        return
    move(n-1, a, c, b)          #   1、先将(N-1) 个圆盘移动到 b
    print (a, '-->' , c)        #   2、再将最下面的一个圆盘由a移动到c
    move(n-1, b, a, c)          #   3、最后将b圆盘上的(N-1) 个圆盘移动到c上

move(4, 'A', 'B', 'C')

print ("\n---------------5、Python之定义默认函数--------------------");
#   由于函数的参数按从左到右的顺序匹配，所以默认参数只能定义在必需参数的后面：
'''
例题：
请定义一个 greet() 函数，它包含一个默认参数，
如果没有传入，打印 'Hello, world.'，
如果传入，打印 'Hello, xxx.'
'''
def greet(name='world'):
    print ('hello,'+name);

greet()
greet('Bart')

print ("\n---------------6、Python之定义可变参数函数--------------------");
#   请编写接受可变参数的 average() 函数。
def average(*args):
    sum = 0.0
    if len(args) == 0:
        return sum
    for x in args:
        sum = sum + x
    return sum / len(args)

print (average());
print (average(1,2));
print (average(1,2,3,4));

