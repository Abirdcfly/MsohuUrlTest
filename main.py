# !/usr/bin/env python
# -*- coding:utf-8 -*-

from Thread import init
import datetime
import os
from config import *


def main():
    start_time = datetime.datetime.now()
    print u"开始爬"
    c = init(CHOICE, ROOT_URL, NUMBER_OF_THREADS, FINAL_COUNT, SHOW_VISITED_URL, TIME_OUT, N_LEVEL)
    final_time = datetime.datetime.now()
    log_path = os.path.dirname(__file__) + '/logs/'
    f = open(log_path + 'Test Time.txt', 'a+')
    f.write(str(final_time)
            + '  线程数:' + str(NUMBER_OF_THREADS)
            + '  页数:' + str(c)
            + '  用时:' + str((final_time - start_time).seconds) + 's' + '  ')
    if CHOICE == 1:
        f.write('按层数遍历: ' + str(N_LEVEL) + ' 层'
            + '\n')
    elif CHOICE == 2:
        f.write('按链接数遍历: ' + str(FINAL_COUNT) + ' 页'
                + '\n')
    f.close()

    print u"\n爬取完成.请查看log文件夹"

if __name__ == "__main__":
    main()
