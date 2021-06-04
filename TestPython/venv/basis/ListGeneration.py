# -*- coding: utf-8 -*-

print ("————————————— 八、列表生成式————————————————");
print ("\n---------------1、生成列表--------------------");
'''
请利用列表生成式生成列表 [1x2, 3x4, 5x6, 7x8, ..., 99x100]
提示：range(1, 100, 2) 可以生成list [1, 3, 5, 7, 9,...]
'''
print ([ x * (x+1) for x in list(range(1,100,2)) ]);

print ("\n---------------2、复杂表达式--------------------");
'''
在生成的表格中，对于没有及格的同学，请把分数标记为红色。
提示：红色可以用 <td style="color:red"> 实现。
'''
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
def generate_tr(name, score):
    if score < 60:
        return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
    return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)

tds = [generate_tr(name, score) for name, score in d.items()]
print ('<table border="1">')
print ('<tr><th>Name</th><th>Score</th><tr>')
print ('\n'.join(tds))
print ('</table>')

print ("\n---------------3、条件过滤--------------------");
'''
请编写一个函数，它接受一个 list，然后把list中的所有字符串变成大写后返回，非字符串元素将被忽略。
提示：
1. isinstance(x, str) 可以判断变量 x 是否是字符串；
2. 字符串的 upper() 方法可以返回大写的字母。
'''
def toUppers(L):
    return [ x.upper() for x in L if isinstance(x, str) ]

print (toUppers(['Hello', 'world', 110]));

print ("\n---------------4、多层表达式--------------------");
'''
利用 3 层for循环的列表生成式，找出对称的 3 位数。例如，121 就是对称数，因为从右到左倒过来还是 121。
'''
print ([ 100 * n1 + 10 * n2 + n3
         for n1 in list(range(1,10))
         for n2 in list(range(0,10))
         for n3 in list(range(0,10))
         if n1 == n3 ]);

