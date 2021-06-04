# -*- coding: utf-8 -*-
print ("—— 七、Python爬虫实战演练：爬取百度百科1000个页面的数据 ——");
print ("—— 7.2、调度程序 ——");

print ("————— Python爬虫：1、总教程程序 ———————————————");

from Reptilian.baike_spider import url_manager, html_downloader, html_parser, html_outputer

class SpiderMain(object):
    # 构造函数初始化各个对象
    def __init__(self):
        self.urls = url_manager.UrlManager()                    # Url管理器
        self.downloader = html_downloader.HtmlDownloader()      # 下载器
        self.parser = html_parser.HtmlParser()                  # 解析器
        self.outputer = html_outputer.HtmlOutputer()            # 输出器

    # 爬虫的调度程序
    def craw(self, root_url):
        # 添加辅助信息，用count判断当前爬取的是第几个url
        count = 1
        # 入口url添加到管理器
        self.urls.add_new_url(root_url)
        # (如果有待爬取的url)遍历url管理器获取url
        while self.urls.has_new_url():
            try:
                # 获取一个待爬取的url(当前爬取的url)
                new_url = self.urls.get_new_url()
                print ('craw %d : %s' % (count, new_url) )
                # 启动下载器下载页面(页面数据)
                html_cont = self.downloader.download(new_url)
                # 下载好页面，调用解析器解析页面数据-->得到新的url列表和新的数据
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                # url添加进url管理器；收集数据
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 20:
                    break
                count = count + 1
            except:
                print ('craw failed')

        # 输出收集好的数据
        self.outputer.output_html()

# 1、编写main函数
if __name__=="__main__":
    # 编写入口url
    root_url = "https://baike.baidu.com/item/Python/407313"
    # 创建spider
    obj_spider = SpiderMain()
    # 启动爬虫
    obj_spider.craw(root_url)