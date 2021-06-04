# coding=utf-8
# 文件练习1

import configparser

# 创建一个对象
cfg = configparser.ConfigParser()
# 读取文件
cfg.read('imoocFileTest.txt')
#print(cfg.sections())       # ['userinfo', 'study']
# 遍历文件条目内容
# for se in cfg.sections():
#     print(se)
#     print(cfg.items(se))

# 修改条目没人内容
#cfg.set('userinfo', 'pwd', '123456')
# for se in cfg.sections():
#     print(se)
#     print(cfg.items(se))

# 添加新内容
# cfg.set('userinfo', 'email', 'user@mooc.com')
# for se in cfg.sections():
#     print(se)
#     print(cfg.items(se))

# 删除条目
# cfg.remove_option('userinfo', 'email')
# for se in cfg.sections():
#     print(se)
#     print(cfg.items(se))

# 下面内容接study.py