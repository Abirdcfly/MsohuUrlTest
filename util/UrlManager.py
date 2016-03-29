# !/usr/bin/env python
# -*- coding:utf-8 -*-

from QueueExtend import SetUniqueQueue


class UrlManager(object):
    def __init__(self):
        self.new_urls = SetUniqueQueue()  # 程序运行中一直变换的临时链接队列
        self.visited_urls = set()
        self.timeout_urls = set()

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.visited_urls:
            self.new_urls.put(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return self.new_urls.qsize() != 0

    def get_new_url(self):
        new_url = self.new_urls.get(block=True, timeout=0.5)
        self.visited_urls.add(new_url)
        return new_url

    def add_wrong_url(self, wrong_url):
        self.timeout_urls.add(wrong_url)

    def has_wrong_url(self):
        return len(self.timeout_urls) != 0

    def show_urls(self):
        return self.new_urls

    def num_new_url(self):
        return self.new_urls.qsize()

    def num_visited_url(self):
        return len(self.visited_urls)

    def get_visited_url(self):
        return self.visited_urls.pop()
