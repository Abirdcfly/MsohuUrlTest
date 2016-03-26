# -*- coding:utf-8 -*-

# from bs4 import BeautifulSoup
# import urlparse
# import re
#
# soup = BeautifulSoup(open('./test.html'), 'html.parser', from_encoding='utf-8')
# # test = soup.find_all('a', href=re.compile(r"\w*wiki/pro.html?id=\d+"))
# test = soup.find_all('a') #href=re.compile(r"[^wot]")
#
# print "length", len(test)
# for i in test:
#     print i
#
#
# import urllib2
# import urlparse
#
# url = 'http://wot.kongzhong.com/wiki/xml/proList.xml'
# respone = urllib2.urlopen(url)
# # print respone.read()
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(respone, 'html.parser', from_encoding='utf-8')
# # print soup.contents
# # tank = soup.find_all('tankid')
# link = soup.find('tankid')
# print 'www.baidu.com/'+''.join(link.contents)
# print urlparse.urljoin('http://wot.kongzhong.com/wiki/xml/1329.xml', ''.join(link.contents)+'.xml')
# # print(soup.prettify())
# # print soup
#
# print 'abc'.replace('a','')
#
# page_url = 'http://wot.kongzhong.com/wiki/xml/1329.xml'
# a = page_url.replace('http://wot.kongzhong.com/wiki/xml/', '').replace('.xml', '')
# print a

# import urllib2
# # from bs4 import BeautifulSoup
# url = 'http://m.sohu.com/u/vw/83236660.shtml?channeled=1211020100&aid=1000000551308&boke=1'
# http_message = urllib2.urlopen(url).getcode()
# print http_message
# print urllib2.urlopen(url).read()
# content = urllib2.urlopen(url).read()
# soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')

# print soup
# for link in soup.find_all('a'):
#     link_href = str(link.get('href'))
#     if link_href.startswith('/'):
#         new_url = 'http://m.sohu.com'+''.join(link_href)
#     elif link_href.startswith('http://m.sohu.com'):
#         new_url = link_href
#     print new_url
# print http_message,content

# print str(
# import urllib2
# url = u'http://m.sohu.com/subTag/情感恋爱'
# url = url.encode('utf-8')
# content = urllib2.quote(url)
# res = urllib2.urlopen(url)

# url = url.encode("UTF-8")
# # urllib2.quote()
# urllib2.urlopen(url)

# import urllib2
# url = u"http://www.baidu.com/wd=测试"
# urllib2.urlopen(url.encode('utf-8')).read()

# import time
# import os.path
# def getLogsPath():
#     log_path = os.path.dirname(__file__) + '/logs/'
#     if(not os.path.exists(log_path)):
#         os.mkdir(log_path)
#     return log_path
# datas={'a':2,'b':3}
# path = getLogsPath()
# localtime = time.asctime(time.localtime(time.time()))
# f = open(path + str(time.strftime('%Y-%m-%d %H-%M-%S')+'.txt'), 'a+')
# for i,j in datas.items():
#     f.write('%s:%s'%(i,j))
#     f.write('\n')


# !/usr/bin/env python
# -*- coding:utf-8 -*-
# aurl = 'http://m.sohu.com/f/MNz6bia/?_once_=000144_bst02'
# from bs4 import BeautifulSoup
# import urlparse
# import re
#
#
# class Parser(object):
#     def _pre_test(self, url, soup):
#         bad_links = {}
#         if soup.title == "手机搜狐":
#             bad_links[url] = 404
#             return False
#         return True
#
#     def _get_new_urls(self, soup):
#         new_urls = []
#         for link in soup.find_all('a'):
#             # todo: 删掉这个try
#             # try:
#             link_href = unicode(link.get('href')).encode('utf-8')
#             # except:
#             #     print link.get('href')
#             # todo:处理外链
#             if link_href.startswith('/'):
#                 new_url = 'http://m.sohu.com'+''.join(link_href)
#             elif link_href.startswith('http://m.sohu.com'):
#                 new_url = link_href
#             # else:
#             #     break
#             try:
#                 new_urls.append(new_url)
#             except:
#                 print u'外链', link_href
#         return new_urls
#
#     def parse(self, page_url, html_content):
#         if html_content is None:
#             return
#         soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
#         if self._pre_test(page_url, soup):
#             new_urls = self._get_new_urls(soup)
#             return new_urls
#         else:
#             return
# ###################################################
# import urllib2
# class Downloader(object):
#     def test(self,url):
#         bad_links = {}
#         if url is None:
#             return "None"
#         http_message = urllib2.urlopen(url).getcode()
#         if http_message != 200:
#             bad_links[url] = http_message
#         return http_message, bad_links
#
#     def download(self, url):
#         if url is None:
#             return None
#         try:
#             response = urllib2.urlopen(url)
#         except urllib2.HTTPError, error:
#             print error.read()
#         return response.read()
#
#
#
# p = Parser()
# d = Downloader()
# # print d.download(aurl)
#
# html_content = d.download(aurl)
# new_urls = p.parse(aurl, html_content)
# print new_urls

import urllib2
url = u"http://m.sohu.com/f/3ye6fya/"
urllib2.urlopen(url.encode('utf-8')).read()
