# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
# items.py定义Item数据结构的文件

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 明确抓取目标：抓取豆瓣电影top250的信息。https://movie.douban.com/top250
    # 序号
    serial_number = scrapy.Field();
    # 电影的名称
    movie_name = scrapy.Field()
    # 电影的介绍
    introduce = scrapy.Field()
    # 星级
    star = scrapy.Field()
    # 电影的评论数
    evaluate = scrapy.Field()
    # 电影的描述
    describe = scrapy.Field()


