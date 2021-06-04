# -*- coding: utf-8 -*-
print ("—— 七、Python爬虫实战演练：爬取百度百科1000个页面的数据 ——");
print ("—— 7.2、调度程序 ——");

print ("————— Python爬虫：2、URL管理器 ——————————————");

class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    # 向管理器中添加一个新的url
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    # 向管理器中添加批量的url
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)


    # 判断管理器中是否有新的待爬取的url
    def has_new_url(self):
        return len(self.new_urls) != 0

    # 从url管理器中获取一个新的待爬取的url
    def get_new_url(self):
        new_url = self.new_urls.pop() # pop()方法会获取一个url并移除url
        self.old_urls.add(new_url)
        return new_url

