# !/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib2
import socket

class Downloader(object):
    # def test(self,url):
    #     http_message = 0
    #     bad_links = {}
    #     if url is None:
    #         return
    #     # todo: ?
    #     try:
    #         http_message = urllib2.urlopen(url).getcode()
    #         if http_message != 200:
    #             bad_links[url] = http_message
    #     except urllib2.HTTPError, error:
    #         bad_links[url] = error.code
    #     return http_message, bad_links

    def download(self, url):
        bad_links = {}
        state = True
        if url is None:
            return None
        try:
            response = urllib2.urlopen(url, timeout=5)
            return state, response.read()
        except urllib2.HTTPError, error:
            bad_links[url] = error.code
            state = False
            return state, bad_links
        except socket.timeout:
            bad_links[url] = '  time_out'
            state = False
            return state, bad_links
        # todo:处理加载慢的链接