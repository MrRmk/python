# -*- coding: utf-8 -*-
print ("—— 七、Python爬虫实战演练：爬取百度百科1000个页面的数据 ——");
print ("—— 7.2、调度程序 ——");

print ("————— Python爬虫：3、网页下载器 ———————————————");

import urllib.request

class HtmlDownloader(object):


    def download(self, url):
        if url is None:
            return
        response = urllib.request.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()

