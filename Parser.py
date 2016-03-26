# !/usr/bin/env python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import urlparse
import re


class Parser(object):
    def _pre_test(self, url, soup):
        bad_links = {}
        if soup.title == "手机搜狐" and url != 'http://m.sohu.com':
            bad_links[url] = 404
            # todo:坏链处理。。。
            return False, bad_links
        return True, None
    # todo:js去掉

    def _get_new_urls(self, soup):
        new_urls = []
        for link in soup.find_all('a'):
            # todo: 删掉这个try
            # try:
            link_href = unicode(link.get('href')).encode('utf-8')
            # except:
            #     print link.get('href')
            # todo:处理外链
            if link_href.startswith('/'):
                new_url = 'http://m.sohu.com'+''.join(link_href)
            elif link_href.startswith('http://m.sohu.com'):
                new_url = link_href
            # else:
            #     break
            try:
                new_urls.append(new_url)
            except:
                print u'外链', link_href
        return new_urls

    def parse(self, page_url, html_content):
        if html_content is None:
            return
        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
        state, bad_links = self._pre_test(page_url, soup)
        if state:
            new_urls = self._get_new_urls(soup)
            return True, new_urls
        else:
            return False, bad_links
