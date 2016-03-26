# !/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import os.path

class Outputer(object):
    def __init__(self):
        self.datas = {}

    def collect_data(self, data):
        if data is None:
            return
        self.datas.update(data)

    def output_txt(self, pages):
        path = self._getLogsPath()
        creat_time = time.strftime('%Y-%m-%d %H-%M-%S')
        f = open(path + str(creat_time)+'.txt', 'a+')
        f.write(str(creat_time) + '\n')
        if self.datas:
            for i, j in self.datas.items():
                f.write('%s:%s' % (i, j) + '\n')
        else:
            f.write("共扫描 %d 个页面，未发现错误！"% pages)


    def output_html(self):
        fout = open('result.htm', 'w')
        fout.write("<html>")
        fout.write("<head>")
        fout.write('<meta charset="utf-8"></meta>')
        fout.write("<title>Crawl Result</title>")
        fout.write("</head>")
        fout.write("<body>")
        fout.write('<h1 style="text-align:center">Crawl Result</h1>')
        fout.write('<table style="border-collapse:collapse;"  border="1">')
        for data in self.datas:
            fout.write("<tr>")
            #            fout.write("<td><a href = '%s'>" % data["url"])
            #            fout.write("%s</a></td>" % data["title"].encode("utf-8"))
            fout.write("<td><a href='%s'>%s</a></td>" % (data["url"].encode("utf-8"), data["title"].encode("utf-8")))
            fout.write("<td>%s</td>" % data["summary"].encode("utf-8"))
            fout.write("</tr>")
        fout.write("</table>")
        fout.write('<br /><br /><p style="text-align:center">Power By Effortjohn</p>')
        fout.write("</body>")
        fout.write("</html>")

    def _getLogsPath(self):
        log_path = os.path.dirname(__file__) + '\\logs\\'
        if(not os.path.exists(log_path)):
            os.mkdir(log_path)
        return log_path