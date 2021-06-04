# -*- coding: utf-8 -*-
print ("—— 七、Python爬虫实战演练：爬取百度百科1000个页面的数据 ——");
print ("—— 7.2、调度程序 ——");

print ("————— Python爬虫：4、html网页解析器 ———————————————");

from bs4 import BeautifulSoup
import re
import urllib.parse

class HtmlParser(object):

    # 页面中所有其他的搜词条的url
    def _get_new_urls(self, page_url, soup):
        # 定义一个new_urls的列表，将新的url放入new_urls列表
        new_urls = set()
        # 得到所有词条url--links  例如： /item/Python/407313
        links = soup.find_all('a', href=re.compile(r"/item/.+/\d"))
        for link in links:
            new_url = link['href']
            # 拼接完整的url -- 会将new_url按照page_url的格式拼接成一个新的url
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    # 解析页面数据
    def _get_new_data(self, page_url, soup):
        res_data = {}

        # url
        res_data['url'] = page_url

        # <dd class="lemmaWgt-lemmaTitle-title">  <h1>Python</h1>
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()

        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()

        return res_data

    # 解析器传入一个url和下载好页面的数据html_cont
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,
                             'html.parser',
                             # from_encoding='utf-8'
                             )
        new_urls = self._get_new_urls(page_url, soup)   # 解析出新的url
        new_data = self._get_new_data(page_url, soup)   # 解析出新的数据
        return new_urls, new_data

