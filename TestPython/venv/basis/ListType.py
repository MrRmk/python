# -*- coding: utf-8 -*-
print ("————————————— 二、Python之List和Tuple类型————————————————");
print ("\n---------------1、List类型--------------------");
#假设班里有3名同学：Adam，Lisa和Bart，他们的成绩分别是 95.5，85 和 59，
# 请按照 名字, 分数, 名字, 分数... 的顺序按照分数从高到低用一个list表示，然后打印出来。
L = ['Adam', 95.5, 'Lisa', 85, 'Bart', 59 ];
print (L);

print ("\n---------------2、索引遍历输出--------------------");
#使用索引时，千万注意不要越界。否则会报错。
L = [95.5, 85, 59];
print(L[0])
print(L[1])
print(L[2])

print ("\n---------------3、倒序索引--------------------");
#使用倒序索引时，也要注意不要越界。
L = [95.5, 85, 59]
print (L[-1]);
print (L[-2]);
print (L[-3]);

print ("\n---------------4、添加新元素——append()和insert()方法--------------------");
#insert()方法以索引位置0开始
#假设新来一名学生Paul，Paul 同学的成绩比Bart好，但是比Lisa差，他应该排到第三名的位置，请用代码实现。
L = ['Adam', 'Lisa', 'Bart'];
L.insert(2, 'Paul');
print(L);

print ("\n---------------5、List删除元素——pop()方法--------------------");
#pop()方法以索引位置0开始
L = ['Adam', 'Lisa', 'Paul', 'Bart']
L.pop(2);
print(L)

print ("\n---------------6、List替换元素--------------------");
L = ['Adam', 'Lisa', 'Bart']
L[2] = 'Paul';
print(L);
L[-1] = 'Bart';
print(L);

print ("\n---------------7、Python之创建tuple--------------------");
#tuple是另一种有序的列表，中文翻译为“ 元组 ”。tuple 和 list 非常类似，但是，tuple一旦创建完毕，就不能修改了。
#创建tuple和创建list唯一不同之处是用( )替代了[ ]。
t = ('Adam', 'Lisa', 'Bart');
print(t);

print ("\n---------------8、Python之创建单元素tuple--------------------");
t = ();
print(t);
t = (1);
print(t);
t = (1,);   #为了避免歧义的正确单元素tuple表示
print(t);

print ("\n---------------Python之“可变”的tuple--------------------");
t = ('a', 'b', ['A', 'B']);
print(t);
L = t[2];
L[0] = 'X';
L[1] = 'Y';
print(t);
#定义了tuple：
#t = ('a', 'b', ['A', 'B'])
#由于 t 包含一个list元素，导致tuple的内容是可变的。能否修改上述代码，让tuple内容不可变？
t = ('a', 'b', ('A', 'B'));
print (t);