# -*- coding: utf-8 -*-

print ("————————————— Python进阶学习————————————————");
print ("————————————— 五、定制类 ————————————————");

print ("\n————————————— 1、python中__str__和__repr__  ————————————————");
'''
请给Student 类定义__str__和__repr__方法，使得能打印出<Student: name, gender, score>：
class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score
'''
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score
    def __str__(self):
        return '(Student: %s,%s,%d)' % (self.name, self.gender, self.score)
        __repr__ = __str__
s = Student('bob', 'male', 88)
print (s)

print ("\n————————————— 2、python中__cmp__  ————————————————");
'''
请修改 Student 的 __cmp__ 方法，让它按照分数从高到底排序，分数相同的按名字排序。
'''
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return '(%s: %s)' % (self.name, self.score)

    __repr__ = __str__

    def __cmp__(self, s):
        if self.score < s.score:
            return 1
        elif self.score > s.score:
            return -1
        elif self.name < s.name:
            return -1
        elif self.name > s.name:
            return 1
        else:
            return 0
    def __cmp__(self, s):
        if self.score == s.score:
            return cmp(self.name, s.name)
        return -cmp(self.score,s.score)

L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 99)]
# 在lambda函数里，-x.score代表分数降序，x.name代表名字升序
print (sorted(L, key=lambda student:(-student.score,student.name)))

print ("\n————————————— 3、python中__len__ ————————————————");
'''
斐波那契数列是由 0, 1, 1, 2, 3, 5, 8...构成。
请编写一个Fib类，Fib(10)表示数列的前10个元素，print Fib(10) 可以打印出数列的前 10 个元素，len(Fib(10))可以正确返回数列的个数10。
'''
class Fib(object):
    def __init__(self, num):
        self.num = num
        self.fibo = [0, 1]
        i = 2
        while i < self.num:
            self.fibo.append(self.fibo[i - 2] + self.fibo[i - 1])
            i += 1
    def __str__(self):
        return str(self.fibo)
    def __len__(self):
        return len(self.fibo)

f = Fib(10)
print (f)
print (len(f))

print ("\n————————————— 4、python中数学算法 ————————————————");
'''
Rational类虽然可以做加法，但无法做减法、乘方和除法，请继续完善Rational类，实现四则运算。
提示：
减法运算：__sub__
乘法运算：__mul__
除法运算：__div__
'''
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)
    def __sub__(self, r):
        return Rational(self.p * r.q - self.q * r.p, self.q * r.q)
    def __mul__(self, r):
        return Rational(self.p * r.p, self.q * r.q)
    def __truediv__(self, r):
        return Rational(self.p * r.q, self.q * r.p)
    def __str__(self):
        # 求公约数，运算结果除以最大公约数得最简分数
        if self.p < self.q:
            k = self.p
        else:
            k = self.q
        for x in range(k, 0, -1):
            if self.p % x == 0 and self.q % x == 0:
                self.p = self.p / x
                self.q = self.q / x
                break
        return '%s/%s' % (self.p, self.q)
        '''
        c = gcd(self.p, self.q)
        return '%s/%s' % (self.p/c, self.q/c)
        '''
    __repr__ = __str__

r1 = Rational(1, 2)
r2 = Rational(1, 4)
print (r1 + r2)
print (r1 - r2)
print (r1 * r2)
print (r1 / r2)

print ("\n————————————— 5、python中类型装换 ————————————————");
'''
请继续完善Rational，使之可以转型为float。
'''
class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
    def __int__(self):
        return self.p // self.q
    def __float__(self):
        return float(self.p) / self.q
print (float(Rational(7, 2)))
print (float(Rational(1, 3)))

print ("\n————————————— 6、python中@property（类的属性） ————————————————");
'''
如果没有定义set方法，就不能对“属性”赋值，这时，就可以创建一个只读“属性”。
请给Student类加一个grade属性，根据 score 计算 A（>=80）、B、C（<60）。
'''
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score
    @property
    def grade(self):
        if self.__score >= 80:
            return 'A'
        elif self.__score < 60:
            return 'C'
        else:
            return 'B'
s = Student('Bob', 59)
print (s.grade)
s.score = 60
print (s.grade)
s.score = 99
print (s.grade)


print ("\n————————————— 7、python中__slots__（类允许的属性列表） ————————————————");
'''
假设Person类通过__slots__定义了name和gender，请在派生类Student中通过__slots__继续添加score的定义，使Student类可以实现name、gender和score 3个属性。
'''
class Person(object):
    __slots__ = ('name', 'gender')
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
class Student(Person):
    __slots__ = ('name', 'gender', 'score')
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score
s = Student('Bob', 'male', 59)
s.name = 'Tim'
s.score = 99
print (s.score)

print ("\n————————————— 8、python中__call__（函数其实是一个对象） ————————————————");
'''
改进一下前面定义的斐波那契数列：
class Fib(object):
    ???
请加一个__call__方法，让调用更简单：
>>> f = Fib()
>>> print f(10)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
'''
class Fib(object):
    def __init__(self):
        pass
    def __call__(self, num):
        self.fibo = [0, 1]
        i = 2
        while i < num:
            self.fibo.append(self.fibo[i - 2] + self.fibo[i - 1])
            i += 1
        return self.fibo
f = Fib()
print (f(10))