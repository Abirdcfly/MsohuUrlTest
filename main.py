# !/usr/bin/env python
# -*- coding:utf-8 -*-
from Outputer import Outputer
from Downloader import Downloader
from UrlManager import UrlManager
from Parser import Parser


class WebTestMain(object):
    def __init__(self):
        self.page_count = 1

    def craw(self, root_url):
        # todo: 层数设置？
        page_count = self.page_count
        UrlManager.add_new_url(root_url)
        try:
            while UrlManager.has_new_url():
                todo_url = UrlManager.get_new_url()
                try:
                    print u"\nNO: %d 正在检测链接:%s" % (page_count, todo_url)
                except:
                    print u"出错", todo_url
                    # todo: 换成 contiune 是不是更好？
                # page_status, bad_links = Downloader.test(todo_url)
                # print u"\n结果：%s" % page_status
                # todo: 加入状态码的说明
                state, content = Downloader.download(todo_url)
                if state:
                    prase_state, new_urls = Parser.parse(todo_url, content)
                    if prase_state:
                        UrlManager.add_new_urls(new_urls)
                    else:
                        Outputer.collect_data(new_urls)
                else:
                    Outputer.collect_data(content)
                page_count += 1
                # except:
                #     print u"页面爬取失败"
                #     UrlManager.add_wrong_url(todo_url)
                # todo:测试代码
                if page_count == 5000:
                    self.page_count = page_count
                    break
                print UrlManager.num_new_url()
        finally:
            Outputer.output_txt(self.page_count)
        # Outputer.output_txt(self.page_count)
        # todo:加入数据库？还是？

    def show(self):
        pass
    # todo: 将效果显示到页面。


if __name__ == "__main__":
    print u"开始爬"
    root_url = 'http://m.sohu.com'
    # root_url = 'http://m.sohu.com/f/MNz6bia/?_once_=000144_bst02'
    WebTestMain = WebTestMain()
    UrlManager = UrlManager()
    Downloader = Downloader()
    Parser = Parser()
    Outputer = Outputer()
    WebTestMain.craw(root_url)
    print u"\n爬取完成.是否显示页面？"
    # show_result = raw_input(u'输入Y来显示页面。其他字符退出>')
    # if show_result == 'Y' or show_result == 'y' or show_result == 'Yes':
    #     WebTestMain.show()
    # else:
    #     exit()
    # todo: 有没有更优雅的写法？
