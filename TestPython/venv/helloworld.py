# -*- coding: utf-8 -*-

'''
help()  #查看python版本
#在所执行文件的根目录下的"data"这个文件夹下的“_init_.py”中导入"CreateDataLoader"
from data import CreateDataLoader
#在所执行文件的根目录下的"data"这个文件夹下的“aligned_dataset”中导入"AlignedDataset"
from data.aligned_dataset import AlignedDataset
总结：1、如果 from 后面是 “X” 而非 “X.Y”的形式，则所导入的模块在该文件夹下的 “_init_.py”中;
      2、如果 from 后面是 “X.Y” 而非 “X”的形式，则所导入的模块在该文件夹下的 “Y.py”中;
'''

print ("\n--------------- 一、Python变量和数据类型 --------------------");
print ("\n---------------1、--------------------");
print ("helloworld");
print ("这是测试的python语句");


print ("\n---------------2、--------------------");
print (not False);  #   True
print (not True);   #   False

print ("\n---------------3、--------------------");
print (1 + 2);      #   3
print (1 + 2.0);    #   3.0
print (10 / 4);     #   2（输出结果有问题）
print (10 % 4);     #   2.5

print ("\n---------------4、--------------------");
a = 123;
#print (a);
a = "imooc";
print (a);          #   imooc

print ("\n---------------5、--------------------");
print ("hello","world");    #逗号代表一个空格    `hello world

print ("\n---------------6、--------------------");
print ('这是学习\'python\'的一条"测试"语句');  #用 \ 表示转义

print("\n---------------7、--------------------");
print (r'这是学习"python"的一条"测试"语句');
# 如果一个字符串包含很多需要转义的字符，对每一个字符都进行转义会很麻烦。
# 为了避免这种情况，我们可以在字符串前面加个前缀 r，表示这是一个 raw 字符串

print ("\n---------------8、--------------------");
print ('''窗前明月光，
疑是地上霜。
举头邀明月，
低头思故乡。''');     #多行字符串'''......'''

print ("\n---------------9、--------------------");
print (u'中文');      #以Unicode表示的字符串用u'...'

print ("\n---------------10、--------------------");
a = True;
print (a and 'a=T' or 'a=F');       #   a=T
a = 'python';
print("hello,",a or 'world');       #   hello, python
b = '';
print('hello,', b or 'world');      #   hello, world
#因为Python把0、空字符串''和None看成 False，其他数值和非空字符串都看成 True
