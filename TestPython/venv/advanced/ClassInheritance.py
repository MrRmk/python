# -*- coding: utf-8 -*-

print ("————————————— Python进阶学习————————————————");
print ("————————————— 四、类的继承 ————————————————");

print ("\n————————————— 1、python中继承一个类  ————————————————");
'''
请参考 Student 类，编写一个 Teacher类，也继承自 Person。
'''
class Person(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course

t = Teacher('Alice', 'Female', 'English')
print (t.name)
print (t.gender)
print (t.course)

print ("\n————————————— 2、python中判断类型  ————————————————");
'''
请根据继承链的类型转换，依次思考 t 是否是 Person，Student，Teacher，object 类型，并使用isinstance()判断来验证您的答案。
'''
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score
class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course
t = Teacher('Alice', 'Female', 'English')

print (isinstance(t, Person))
print (isinstance(t, Student))
print (isinstance(t, Teacher))
print (isinstance(t, object))

print ("\n————————————— 3、python中多态  ————————————————");
'''
Python提供了open()函数来打开一个磁盘文件，并返回 File 对象。File对象有一个read()方法可以读取文件内容：
例如，从文件读取内容并解析为JSON结果：
import json
f = open('/path/to/file.json', 'r')
print json.load(f)
由于Python的动态特性，json.load()并不一定要从一个File对象读取内容。任何对象，只要有read()方法，就称为File-like Object，都可以传给json.load()。

请尝试编写一个File-like Object，把一个字符串 r'["Tim", "Bob", "Alice"]'包装成 File-like Object 并由 json.load() 解析。
'''
import json
class Students(object):
    def __init__(self, strlist):
        self.strlist = strlist
    def read(self):
        return (self.strlist)
s = Students('["Tim", "Bob", "Alice"]')
print (json.load(s))

print ("\n————————————— 4、python中多重继承 ————————————————");
'''
+-Person
  +- Student
  +- Teacher
是一类继承树；
+- SkillMixin
   +- BasketballMixin
   +- FootballMixin
是一类继承树。
通过多重继承，请定义“会打篮球的学生”和“会踢足球的老师”。
'''
class Person(object):
    pass
class Student(Person):
    pass
class Teacher(Person):
    pass
class SkillMixin(object):
    pass
class BasketballMixin(SkillMixin):
    def skill(self):
        return 'basketball'
class FootballMixin(SkillMixin):
    def skill(self):
        return 'football'
class BStudent(Student, BasketballMixin):
    pass
class FTeacher(Teacher, FootballMixin):
    pass
s = BStudent()
print (s.skill())

t = FTeacher()
print (t.skill())

print ("\n————————————— 5、python中获取对象信息 ————————————————");
'''
对于Person类的定义：
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
希望除了 name和gender 外，可以提供任意额外的关键字参数，并绑定到实例，请修改 Person 的 __init__()定 义，完成该功能。
'''
class Person(object):
    def __init__(self, name, gender, **kw):
        self.name = name
        self.gender = gender
        for k,v in kw.items():
            setattr(self, k, v)
p = Person('Bob', 'Male', age=18, course='Python')
print (p.age)
print (p.course)
print (p)