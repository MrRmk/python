# -*- coding: utf-8 -*-

print ("————————————— Python进阶学习————————————————");
print ("————————————— 三、面向对象编程基础————————————————");

print ("\n————————————— 1、python之定义类并创建实例  ————————————————");
'''
请练习定义Person类，并创建出两个实例，打印实例，再比较两个实例是否相等。
'''
#   定义类
class Person(object):
    pass
#   创建实例
xiaoming = Person()
xiaohong = Person()

print (xiaoming)
print (xiaohong)
print (xiaoming == xiaohong)

print ("\n————————————— 2、python中创建实例属性  ————————————————");
'''
请创建包含两个 Person 类的实例的 list，并给两个实例的 name 赋值，然后按照 name 进行排序。
'''
class Person(object):
    pass
p1 = Person()
p1.name = 'Bart'

p2 = Person()
p2.name = 'Adam'

p3 = Person()
p3.name = 'Lisa'

L1 = [p1, p2, p3]
L2 = sorted(L1, key = lambda x: x.name)

print (L2[0].name)
print (L2[1].name)
print (L2[2].name)

print ("\n————————————— 3、python中初始化实例属性  ————————————————");
'''
请定义Person类的__init__方法，除了接受 name、gender 和 birth 外，还可接受任意关键字参数，并把他们都作为属性赋值给实例。
'''
class Person(object):
    def __init__(self, name, gender, birth, **kw):
        self.name = name
        self.gender = gender
        self.birth = birth
        for k,v in kw.items():
            setattr(self, k, v)
xiaoming = Person('Xiao Ming', 'Male', '1991-1-1', job='Student')
print (xiaoming.name)
print (xiaoming.job)

print ("\n————————————— 4、python中访问权限  ————————————————");
'''
请给Person类的__init__方法中添加name和score参数，并把score绑定到__score属性上，看看外部是否能访问到。
'''
class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score    #相当于私有属性
    def get_score(self):
        return self.__score

p = Person('Bob', 59)
print (dir(p))                 #获取对象p的属性
print (p.__dict__)             #对象在构造函数里面的值的属性
print ('类型：',type(p))                #对象的类型
print (p.name)                 # >>>  {'name': 'Bob', '_Person__score': 59}
print (p.get_score())          #通过自定义get方法访问私有属性
print (p._Person__score)       #访问私有属性
try:
    print (p.__score)
except:
    print ('attributeerror')

print ("\n————————————— 5、python中创建类属性 ————————————————");
'''
请给 Person 类添加一个类属性 count，每创建一个实例，count 属性就加 1，这样就可以统计出一共创建了多少个 Person 的实例。
'''
class Person(object):
    # 设置类属性
    count = 0
    address = 'Earth'
    def __init__(self, name):
        # 实例属性
        self.name = name
        Person.count += 1
p1 = Person('Bob')
print (Person.count)

p2 = Person('Alice')
print (Person.count)

p3 = Person('Tim')
print (Person.count)

print ('Person address = ' + Person.address)
p1.address = 'China'    #实际上是实例p1创建了一个跟类属性address同名的实力属性，并赋值为China,而后面p2和Person调用的还是类属性值Earth
print ('p1 address = ' + p1.address)
print ('p2 address = ' + p2.address)
print ('Person address = ' + Person.address)
Person.address = 'Moon'
print ('\np1 address = ' + p1.address)
print ('p2 address = ' + p2.address)
print ('Person address = ' + Person.address)

print ("\n————————————— 6、python中类属性和实例属性名字冲突怎么办 ————————————————");
'''
请把上节的 Person 类属性 count 改为 __count，再试试能否从实例和类访问该属性。
'''
class Person(object):
    __count = 0
    def __init__(self, name):
        self.name = name
        Person.__count += 1
        print (Person.__count)
p1 = Person('Bob')
p2 = Person('Alice')
try:
    print (Person.__count)
except:
    print ('attributeError')

print ("\n————————————— 7、python中定义实例方法 ————————————————");
'''
请给 Person 类增加一个私有属性 __score，表示分数，再增加一个实例方法 get_grade()，能根据 __score 的值分别返回 A-优秀, B-及格, C-不及格三档。
'''
class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score >= 90:
            return "A-优秀"
            #   return self.name+': A-优秀'
        elif self.score >= 60:
            return "B-及格"
            #   return self.name+': B-及格'
        else:
            return "C-不及格"
            #   return self.name+': C-不及格'
p1 = Person('Bob', 90)
p2 = Person('Alice', 65)
p3 = Person('Tim', 48)

print (p1.get_grade())
print (p2.get_grade())
print (p3.get_grade())

print ("\n————————————— 8、python中方法也是属性 ————————————————");
'''
由于属性可以是普通的值对象，如 str，int 等，也可以是方法，还可以是函数，
大家看看下面代码的运行结果，请想一想 p1.get_grade 为什么是函数而不是方法：
'''
class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.get_grade = lambda: 'A'

p1 = Person('Bob', 90)
print (p1.get_grade)
print (p1.get_grade())

print ("\n————————————— 9、python中定义类方法 ————————————————");
'''
如果将类属性 count 改为私有属性__count，则外部无法读取__score，但可以通过一个类方法获取，请编写类方法获得__count值。
'''
class Person(object):
    __count = 0
    def __init__(self, name):
        self.name = name
        Person.__count += 1
    @classmethod
    def how_many(cls):
        return cls.__count
    @property
    def get_count(self):
        return self.__count
# main函数
if __name__ == '__main__':
    print(Person.how_many())
    p1 = Person('Bob')
    print(Person.how_many())  # 类名调用@classmethod定义的方法
    print(p1.get_count)  # 对象名调用@property定义的方法不加括号，想调用属性一样