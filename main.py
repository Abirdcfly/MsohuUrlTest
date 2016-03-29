# !/usr/bin/env python
# -*- coding:utf-8 -*-

from Thread import init
import datetime
import os
from config import *


def main():
    start_time = datetime.datetime.now()
    print u"开始爬"
    init(ROOT_URL, NUMBER_OF_THREADS, FINAL_COUNT, SHOW_VISITED_URL, TIME_OUT)
    final_time = datetime.datetime.now()
    log_path = os.path.dirname(__file__) + '/logs/'
    f = open(log_path + 'Test Time.txt', 'a+')
    f.write(str(final_time)
            + '  线程数:' + str(NUMBER_OF_THREADS)
            + '  页数:' + str(FINAL_COUNT)
            + '  用时:' + str((final_time - start_time).seconds) + 's'
            + '\n')
    print u"\n爬取完成.请查看log文件夹"

if __name__ == "__main__":
    main()
