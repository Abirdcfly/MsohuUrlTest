# !/usr/bin/env python
# -*- coding:utf-8 -*-

from util.UrlManager import UrlManager
from webtest import WebTestMain
import threading, time


wt = WebTestMain()
UM = UrlManager()


def init(root_url, nthread, final_number, Show_visited_url, time_out):
    if not UM.has_new_url():
        UM.add_new_url(root_url)
        create_thread(nthread, final_number, time_out)
        wt.output_txt(final_number)
        if Show_visited_url:
            show_visited_url(final_number)


def craw(time_out, final_number, id='', delay=0):
    time.sleep(delay)
    while UM.has_new_url() and UM.num_visited_url() <= final_number:
        todo_url = UM.get_new_url()
        print u"\n%s号线程 正在检测链接:%r" % (id,todo_url)
        state, content = wt.download(todo_url, time_out)
        if state:
            prase_state, new_urls = wt.parse(todo_url, content)
            if prase_state:
                UM.add_new_urls(new_urls)
            else:
                wt.collect_data(new_urls)
        else:
            wt.collect_data(content)
        print u'已检查页面数量: ',UM.num_visited_url()
        print u' 剩余页面数量: ',UM.num_new_url()

    # def show():
    #     pass
    # # todo: 将效果显示到页面。


# def create_jobs(root_url):
#
#     # prevent race conditions
#     # tell thread to 'wait its turn'
#     queue.join()
#     crawl()


def create_thread(nthread, final_number, time_out):
    threadsPool = []

    for i in range(nthread):
        t = threading.Thread(target=craw, args=(time_out, final_number, str(i), i+1))
        t.daemon = True
        threadsPool.append(t)

    for i in range(nthread):
        print u'线程 [%s] 启动' % i
        threadsPool[i].start()

    for i in range(nthread):
        threadsPool[i].join()
        print u'线程 [%s] 完成' % i


# def work():
#     while True:
#         link = queue.get()
#         Spider.crawl_page(threading.current_thread().name, link)
#         queue.task_done()
#
#
#
#
# class WebTestThread(threading.Thread):
#     def __init__(self, root_url, final_count, name ='',):
#         threading.Thread.__init__(self)
#         self.name = name
#         self.setDaemon(True)
#         self.root_url = root_url
#         self.final_count = final_count
#         self.webtest = WebTestMain(self.root_url, self.final_count)
#
#     def run(self):
#         self.webtest.craw()
#
#
# class ThreadController(object):
#     def __init__(self, nthread, root_url, final_count):
#         self.threadsPool = []
#         self.nthread = nthread
#         self.root_url =root_url
#         self.final_count =final_count
#
#     def start(self):

        # for i in range(self.nthread):
        #     t = WebTestThread(self.root_url, self.final_count, str(i))
        #     self.threadsPool.append(t)
        #
        # for i in range(self.nthread):
        #     print u'线程 [%s] 启动' % i
        #     self.threadsPool[i].start()
        #
        # for i in range(self.nthread):
        #     self.threadsPool[i].join()
        #     print u'线程 [%s] 完成' % i

# fixme:
def show_visited_url(final_number):
    import os
    log_path = os.path.dirname(__file__) + '/logs/'
    f = open(log_path + str(time.strftime("%Y-%m-%d %H-%M")) + str(final_number) +'_visited_url.txt', 'a+')
    while UM.num_visited_url() >= 1:
        url = UM.get_visited_url()
        f.writelines('\n')
        f.writelines(url)


