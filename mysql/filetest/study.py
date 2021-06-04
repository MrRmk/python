# coding=utf-8
# 文件练习2

import os
import os.path
import configparser
'''
1:  dump ini   显示文件内容
2： del section  删除section
3： del item     显示一个单独的条目
4： modify item  修改一个单独的条目
5： add section  添加section
6： save modify  修改保存到配置文件中
'''
class student_info(object):
    def __init__(self, recordfile):
        # 记录文件名字
        self.logfile = recordfile
        # 创建configparser对象
        self.cfg = configparser.ConfigParser()

    # 自动解析文件
    def cfg_load(self):
        self.cfg.read(self.logfile, 'utf-8')

    # load后的文件显示出来（在内存中，而不是在磁盘中）
    def cfg_dump(self):
        sc_list = self.cfg.sections()
        print("==========================>")
        for se in sc_list:
            print (se)
            print(self.cfg.items(se))
        print("<==========================")

    # 删除一个条目
    def delete_item(self, section, key):
        self.cfg.remove_option(section, key)

    # 删除一个section
    def delete_section(self, section):
        self.cfg.remove_section(section)

    # 添加一个section
    def add_section(self, section):
        self.cfg.add_section(section)

    # 添加/修改一个条目
    def set_item(self, section, key, value):
        self.cfg.set(section, key, value)

    # 保存文件
    def save(self):
        fp = open(self.logfile, 'w')
        self.cfg.write(fp)
        fp.close()

if __name__ == '__main__':
    info = student_info('imoocFiletest.txt')
    info.cfg_load()
    info.cfg_dump()     # 遍历
    info.set_item('userinfo', 'pwd', 'abc')     # 添加/修改一个条目（没有就添加，有就修改）
    info.cfg_dump()     # 遍历
    info.add_section('login')   # 添加一个section
    info.set_item('login', '2015-05-11', '20')   # 添加/修改一个条目（没有就添加，有就修改）
    info.cfg_dump()     # 遍历
    info.save()
