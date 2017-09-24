#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS()
driver.set_window_size(1024, 768)
driver.get('http://zjzone.cc')
doc = driver.page_source

soup = BeautifulSoup(doc, 'lxml')
# 格式化缩进
print soup.prettify()
# 文档信息
print soup.title
print soup.title.string
print soup.p
print soup.a
print soup.find_all('a')
# 提取文档中所有超链接
for link in soup.find_all('a'):
    print link.get('href')

# 按CSS类名进行提取
for link in soup.find_all("a", class_="navbar-brand"):
    print link.get('href')

# 按层级来进行提取
for link in soup.select("body a"):
    print link

# 按是否存在某个属性来提取
for link in soup.select('a[href]'):
    print link