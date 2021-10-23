# !/usr/bin/python
# -*- coding:utf-8 -*-


import os
import re
import time
import random
import requests
import warnings
from bs4 import BeautifulSoup

def main():
    """
    main func
    """
    print "Hello Picture!"
    max_page_num = 30
    all_show_url_list = []
    # 找到所有详情页
    for i in range(random.randint(2, max_page_num - 1), max_page_num):
        url = "https://XXXXX.com/page/%s/" % i
        try:
            page_show_url = get_show_url(url)
            all_show_url_list.extend(page_show_url)
        except Exception as e:
           print "get show url error:%s" % e
           continue

    # 找到所有下载链接
    all_pic_url_list = {}
    for show_url in all_show_url_list:
        try:
            print show_url
            pic_url_list = get_pic_url(show_url)
            # 下载图片到本地
            print download_pic(pic_url_list)
            # 最好持久化到数据库中
            all_pic_url_list[show_url] = pic_url_list
        except Exception as e:
           print "get show url error:%s" % e
           continue
    print all_pic_url_list


def download_pic(pic_url_list, local_path="./output/"):
    """ 下载图片到本地 """
    ret = {
        "success": False,
        "data": ""
    }

    for url in pic_url_list:
        try:
            # download
            headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/'
                                '537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36'
            }
            print url
            pic = requests.get(url, headers=headers, verify=False, timeout=10)
            if pic.status_code != 200:
                print pic.text
                continue
            endfix = url.split("/")[-1]
            local_file = local_path + endfix
            fp = open(local_file, 'wb')
            fp.write(pic.content)
            fp.close()
            time.sleep(random.uniform(0.1, 5))
        except Exception as e:
            print "downlaod %s error: %s" % (url, e)
            continue
    ret["success"] = True
    return ret

def get_pic_url(url):
    """ get pic direct url"""
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/'
                        '537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36'
    }
    pic_url_list = []
    data = requests.get(url, headers=headers, verify=False)
    data = data.text
    soup = BeautifulSoup(data, "html.parser")
    for str_a in soup.find_all('p'):
        try:
            str_a = str(str_a)
            if str_a.find(".jpg") > 0:
                pass
                pic_url = str(str_a).split("src=")[1].split(" ")[0].split("\"")[1]
                pic_url_list.append(pic_url)
        except Exception as e:
            continue
    return pic_url_list

def get_show_url(url):
    """ get girls show path"""
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/'
                        '537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36'
    }
    show_url_list = []
    data = requests.get(url, headers=headers, verify=False)
    data = data.text
    soup = BeautifulSoup(data, "html.parser")
    for str_a in soup.find_all('h2'):
        try:
            show_url = str(str_a).split(" ")[2].split("\"")[1]
            show_url_list.append(show_url)
        except Exception as e:
            continue
    return show_url_list

if __name__ == '__main__':
    main()

