# !/usr/bin/env python
# -*- coding:utf-8 -*-
from Thread import init
import datetime
import os
from config import *


def main():
    init(ROOT_URL, NUMBER_OF_THREADS, FINAL_COUNT, SHOW_VISITED_URL,TIME_OUT)

if __name__ == "__main__":
    start_time = datetime.datetime.now()
    print u"开始爬"
    main()
    print u"\n爬取完成.是否显示页面？"
    final_time = datetime.datetime.now()
    log_path = os.path.dirname(__file__) + '/logs/'
    f = open(log_path + 'Test Time.txt', 'a+')
    f.write(str(final_time)
            + '  线程数:' + str(NUMBER_OF_THREADS)
            + '  页数:' + str(FINAL_COUNT)
            + '  用时:' + str((final_time-start_time).seconds) + 's'
            + '\n')



#
#
#
# queue = Queue()
# Spider(PROJECT_NAME, HOME_PAGE, DOMAIN_NAME)
#
# # If there are items in the queue
# def crawl():
#     queued_links = file_to_set(QUEUE_FILE)
#     link_no = len(queued_links)
#     if link_no > 0:
#         print(str(link_no) + 'links remaining...')
#         create_jobs(queued_links)
#
# def create_jobs(queued_links):
#     for link in queued_links:
#         queue.put(link)
#     # prevent race conditions
#     # tell thread to 'wait its turn'
#     queue.join()
#     crawl()
#
# def create_spiders():
#     for _ in range(NUMBER_OF_THREADS):
#         t = threading.Thread(target=work)
#         # ensures that its a daemon process and dies with main
#         t.daemon = True
#         t.start()
#
# # assign work to the spiders
# def work():
#     while True:
#         link = queue.get()
#         Spider.crawl_page(threading.current_thread().name, link)
#         queue.task_done()
#
# create_spiders()
# crawl()
# WARNING:root:Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.