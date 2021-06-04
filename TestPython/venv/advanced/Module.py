# -*- coding: utf-8 -*-

print ("————————————— Python进阶学习————————————————");
print ("————————————— 二、模块————————————————");

print ("————————————— 1、python之导入模块 ————————————————");
'''
Python的os.path模块提供了 isdir() 和 isfile()函数，请导入该模块，并调用函数判断指定的目录和文件是否存在。
在本机上测试是否存在相应的文件夹和文件。
import os
print (os.path.isdir(r'D:\python\TestPython\venv'))
print (os.path.isfile(r'D:\python\TestPython\venv\helloworld.py'))
'''
import os
print (os.path.isdir(r'D:\python\TestPython\venv'))
print (os.path.isfile(r'D:\python\TestPython\venv\helloworld.py'))

print ("————————————— 2、python中动态导入模块 ————————————————");
'''
利用import ... as ...，还可以动态导入不同名称的模块。
Python 2.6/2.7提供了json 模块，但Python 2.5以及更早版本没有json模块，
不过可以安装一个simplejson模块，这两个模块提供的函数签名和功能都一模一样。
试写出导入json 模块的代码，能在Python 2.5/2.6/2.7都正常运行。
'''
'''
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StirngIO
'''
import json
print (json.dumps({'python':2.7}))
