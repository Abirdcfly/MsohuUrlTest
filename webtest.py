# !/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib2
import urlparse
import socket
from StringIO import StringIO
import gzip
import time
import os.path
from bs4 import BeautifulSoup


class WebTestMain(object):
    def __init__(self):
        self.datas = {}

    def download(self, url, time_out):
        if url is None:
            return None
        bad_links = {}
        state = True

        request = urllib2.Request(url)
        request.add_header('Accept-encoding', 'gzip')
        try:
            response = urllib2.urlopen(request, timeout=time_out)
            if response.info().get('Content-Encoding') == 'gzip':
                buf = StringIO(response.read())
                f = gzip.GzipFile(fileobj=buf)
                data = f.read()
            else:
                data = response.read()
            return state, data
        except (urllib2.HTTPError, urllib2.URLError), error:
            bad_links[url] = error.code
            state = False
            return state, bad_links
        except socket.timeout:
            bad_links[url] = '  time_out'
            state = False
            return state, bad_links

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
            link_href = unicode(link.get('href')).encode('utf-8')
            if link_href.startswith('/'):   # fixme:不确定现在方案和拆分链接比较netloc哪个效率高？
                link_part = urlparse.urlparse(link_href)
                new_url = 'http://m.sohu.com' + ''.join(link_part[2])
                new_urls.append(new_url)
            elif link_href.startswith('http://m.sohu.com'):
                link_part = urlparse.urlparse(link_href)
                new_url = 'http://' + link_part[1] + link_part[2]
                new_urls.append(new_url)
            else:
                continue
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


    def collect_data(self, data):
        if data is None:
            return
        self.datas.update(data)

    def output_txt(self, pages):
        path = self._getLogsPath()
        creat_time = time.strftime('%Y-%m-%d %H-%M-%S')
        f = open(path + str(creat_time) + '.txt', 'a+')
        f.write(str(creat_time) + '\n')
        if self.datas:
            for i, j in self.datas.items():
                f.write('%s:%s' % (i, j) + '\n')
        else:
            f.write("共扫描 %d 个页面，未发现错误！" % pages)


    def _getLogsPath(self):
        log_path = os.path.dirname(__file__) + '/logs/'  # todo 适配win和linux
        if (not os.path.exists(log_path)):
            os.mkdir(log_path)
        return log_path






