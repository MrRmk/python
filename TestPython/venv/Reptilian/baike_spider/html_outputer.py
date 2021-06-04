# -*- coding: utf-8 -*-
print ("—— 七、Python爬虫实战演练：爬取百度百科1000个页面的数据 ——");
print ("—— 7.2、调度程序 ——");

print ("—— Python爬虫：5、将解析到的数据输出保存到文件（方便直接打开查看） ——");

class HtmlOutputer(object):

    def __init__(self):
        # 列表维护收集的数据，构造函数中初始化
        self.datas = []

    # 收集数据
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    # 将收集好的数据写入到一个html中，打开这个页面就能看到所有的数据
    def output_html(self):
        # 建立文件的输出对象fout
        fout = open('output.html', 'w', encoding='utf-8')

        # 向输出对象fout中写入数据
        fout.write("<html><head><meta charset='utf-8'><title>爬取百度百科1000个页面的数据</title></head>")
        fout.write("<body style='margin: 50px auto;width: 80%;'><table border='1px'>")
        fout.write("<tr style='background-color: #d0cccc;'><th>url</th><th>标题</th><th>简介</th></tr>")
        fout.write("<h1 style='text-align: center;'>爬取百度百科1000个页面的数据</h1>")
        # python默认编码是ASCII
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("</tr>")
        fout.write("</table></body></html>")

        # 关闭对象
        fout.close()
