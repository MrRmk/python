# -*- coding: utf-8 -*-
import pymongo
from douban.settings import mongo_host,mongo_port,mongo_db_name,mongo_db_collection

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanPipeline(object):
    def __init__(self):
        host = mongo_host
        port = mongo_port
        dbname = mongo_db_name
        sheetname = mongo_db_collection     #表名
        client = pymongo.MongoClient(host=host,port=port)   #mongoDB的连接
        mydb = client[dbname]               #指定数据库
        self.post = mydb[sheetname]         #

     #数据插入
    def process_item(self, item, spider):
        #获取字典数据，这里的item就是douban_spider.py中yield过来的
        data = dict(item)
        self.post.insert(data)
        return item
