# -*- coding: utf-8 -*-
print ("————————————— 三、Python条件判断与循环————————————————");
print ("\n---------------1、Python之if-else语句--------------------");
score = 55;
if score >= 60:
    print ('passed')
else:
    print ('failed');

print ("\n---------------2、Python之if-elif-else语句--------------------");
#   如果按照分数划定结果：
#   90分或以上：excellent
#   80分或以上：good
#   60分或以上：passed
#   60分以下：failed
#   请编写程序根据分数打印结果。
score = 85;
if score >= 90:
    print ('execllent');
elif score >=80:
    print ('good');
elif score >=60:
    print ('passed');
else:
    print ('failed');

print ("\n---------------3、Python之for循环--------------------");
#   班里考试后，老师要统计平均成绩，已知4位同学的成绩用list表示如下：
#   L = [75, 92, 59, 68]
#   请利用for循环计算出平均成绩。
L = [75, 92, 59, 68]
sum = 0.0
for element in L:
    sum += element
print ('sum =',sum);
print ( 'sum / 4 =',sum / 4 )
# 示例2
L = ['Adam', 'Lisa', 'Bart']
for name in L:
    print (name)

print ("\n---------------4、Python之while循环--------------------");
#   利用while循环计算100以内奇数的和。
sum = 0
x = 1
while x < 100:
    sum += x
    x = x + 2
print (sum)

print ("\n---------------5、Python之break退出循环--------------------");
#   利用 while True 无限循环配合 break 语句，
#   计算 1 + 2 + 4 + 8 + 16 + ... 的前20项的和。
sum = 0
x = 1
n = 1
while True:
    if n > 20:
        break
    sum += x
    x = x * 2
    n += 1
print (sum)

print("\n---------------6、Python之continue继续循环--------------------");
#   对已有的计算 0 - 100 的while循环进行改造，
#   通过增加 continue 语句，使得只计算奇数的和：
sum = 0
x = 0
while True:
    x = x + 1
    if x % 2 == 0:
        continue
    if x > 100:
        break
    sum = sum + x
print (sum)

print ("\n---------------7、Python之多重循环--------------------");
#   对100以内的两位数，请使用一个两重循环
#   打印出所有十位数数字比个位数数字小的数，例如，23（2 < 3）。
for x in [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]:
    for y in [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]:
        if x < y:
            print (x*10+y)

