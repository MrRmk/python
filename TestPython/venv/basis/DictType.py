# -*- coding: utf-8 -*-
print ("————————————— 四、Python中Dict和Set类型————————————————");
print ("\n---------------1、Python之dict(类似结构体)--------------------");
#   新来的Paul同学成绩是 75 分，请编写一个dict，把Paul同学的成绩也加进去。
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59,
    'Paul': 75
}
print (d)

print ("\n---------------2、Python之访问dict--------------------");
#   请打印出：
#   Adam: 95
#   Lisa: 85
#   Bart: 59
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
print ('Adam:',d['Adam'])
print ('Lisa:',d.get('Lisa'))
print ('Bart:',d.get('Bart'))
print ('Paul:',d.get('Paul'))
if 'Adam' in d:
    print (d['Adam'])


print ("\n---------------3、Python之更新dict--------------------");
#   请根据Paul的成绩 72 更新下面的dict：
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
d['Paul'] = 72
print (d)

print ("\n---------------4、Python之遍历dict--------------------");
#   请用 for 循环遍历如下的dict，打印出 name: score 来。
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
for key in d:
    print (key+':',d[key]);

print ("\n---------------5、Python之创建set--------------------");
s = set(['A', 'B', 'C'])
print (s)       # ==>  set(['A', 'B', 'C']) （输出结果有问题）

print ("\n---------------6、Python之访问set--------------------");
s = set(['adam', 'bart', 'paul', 'Lisa'])
print ('adam' in s)     #   True
print ('Bart' in s)     #   False

print ("\n---------------7、Python之set的特点--------------------");
#   月份也可以用set表示，请设计一个set并判断用户输入的月份是否有效。
#   月份可以用字符串'Jan', 'Feb', ...表示。
months = set(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'])
x1 = 'Feb'
x2 = 'Sun'

if x1 in months:
    print ('x1: ok')
else:
    print ('x1: error')

if x2 in months:
    print ('x2: ok')
else:
    print ('x2: error')

print ("\n---------------8、Python之遍历set--------------------");
#   示例1
s = set(['Adam', 'Lisa', 'Bart'])
for name in s:
    print (name)

#   请用 for 循环遍历如下的set，打印出 name: score 来。
s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for x in s:
    print (x[0] + ':', x[1])

print ("\n---------------9、Python之更新set--------------------");
#   更新：即s.add()添加，s.remove()删除

#   例题：针对下面的set，给定一个list，对list中的每一个元素，
#   如果在set中，就将其删除，如果不在set中，就添加进去。
s = set(['Adam', 'Lisa', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for x in L:
    if x in s:
        s.remove(x)
    else:
        s.add(x)
print (s)