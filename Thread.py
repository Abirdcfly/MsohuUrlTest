# !/usr/bin/env python
# -*- coding:utf-8 -*-

from util.UrlManager import UrlManager
from webtest import WebTestMain
import threading
import time


wt = WebTestMain()


def init(choice, root_url, nthread, final_number, Show_visited_url, time_out, n_level):

    if choice == 2:
        bfs(0)
    elif choice == 1:
        bfs(n_level)
    else:
        raise Exception('Wrong Choice '+ str(choice) +' Please edit config.py')

    if not UM[0].has_new_url():
        UM[0].add_new_url(root_url)
        create_thread(choice, n_level, nthread, final_number, time_out)
        c = count(choice, n_level, final_number)
        wt.output_txt(c + 1)  # + m.sohu.com
        if Show_visited_url:
            show_visited_url(choice, n_level, final_number)
        return c


def bfs(n_level):
    UM = []
    global UM
    for _ in range(n_level + 2):
        U = UrlManager()
        UM.append(U)


def craw_level(n_level, time_out, final_number, id='', delay=0):
    i = 0
    time.sleep(delay)
    while i <= n_level:
        while UM[i].has_new_url():
            todo_url = UM[i].get_new_url()
            print u"\n%s号线程 正在检测链接:%r" % (id,todo_url)
            state, content = wt.download(todo_url, time_out)
            if state:
                prase_state, new_urls = wt.parse(todo_url, content)
                if prase_state:
                    if i < n_level:
                        UM[i+1].add_new_urls(new_urls)
                    # todo:最后一层
                else:
                    wt.collect_data(new_urls)
            else:
                wt.collect_data(content)
            print u'已检查页面数量: ',UM[i].num_visited_url()

            if i == n_level:
                print u' 剩余页面数量: ', UM[i].num_new_url()
            else:
                print u' 剩余页面数量: ',UM[i+1].num_new_url()

        print u'\n 第 %s 层检查完成' % i
        i += 1


def craw_number(n_level, time_out, final_number, id='', delay=0):
    time.sleep(delay)
    while UM[0].has_new_url() and UM[0].num_visited_url() <= final_number:
        todo_url = UM[0].get_new_url()
        print u"\n%s号线程 正在检测链接:%r" % (id,todo_url)
        state, content = wt.download(todo_url, time_out)
        if state:
            prase_state, new_urls = wt.parse(todo_url, content)
            if prase_state:
                UM[0].add_new_urls(new_urls)
                # todo:最后一层
            else:
                wt.collect_data(new_urls)
        else:
            wt.collect_data(content)
        print u'已检查页面数量: ',UM[0].num_visited_url()
        print u' 剩余页面数量: ',UM[0].num_new_url()


def create_thread(choice, n_level, nthread, final_number, time_out):
    threadsPool = []

    if choice == 2:
        craw = craw_number
    elif choice == 1:
        craw = craw_level

    for i in range(nthread):
        t = threading.Thread(target=craw, args=(n_level, time_out, final_number, str(i), i+1))
        t.daemon = True
        threadsPool.append(t)

    for i in range(nthread):
        print u'线程 [%s] 启动' % i
        threadsPool[i].start()

    for i in range(nthread):
        threadsPool[i].join()
        print u'线程 [%s] 完成' % i


def show_visited_url(choice, n_level, final_number):
    import os
    log_path = os.path.dirname(__file__) + '/logs/'
    f = open(log_path + str(time.strftime("%Y-%m-%d %H-%M-%S ")) + 'visited_url.txt', 'a+')
    if choice == 2:
        n_level = 1
    for i in range(n_level + 1):
        while UM[i].num_visited_url() >= 1:
            url = UM[i].get_visited_url()
            f.writelines('\n')
            f.writelines(url)


def count(choice, n_level, final_number):
    if choice == 2:
        return final_number
    elif choice == 1:
        tmp = 0
        for i in range(n_level + 1):
            tmp += UM[i].num_visited_url()
        return tmp