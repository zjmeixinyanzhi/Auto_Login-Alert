#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib, urllib2, sys, base64, ssl, json, time

class BaiduAIOCR:

    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key

    def get_access_token(self):
        '''获取access_token'''
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' \
               + self.api_key + '&client_secret=' + self.secret_key
        request = urllib2.Request(host)
        request.add_header('Content-Type', 'application/json; charset=UTF-8')
        response = urllib2.urlopen(request)
        content = response.read()
        if (content):
            return json.loads(content)['access_token']
        else:
            return ''

    def do_recognition(self, access_token, image):
        '获取百度AI识别的图片内容'
        url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general?access_token=' + access_token
        # 二进制方式打开图文件
        f = open(image, 'rb')
        # 参数image：图像base64编码
        img = base64.b64encode(f.read())
        params = {"image": img}
        params = urllib.urlencode(params)
        request = urllib2.Request(url, params)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urllib2.urlopen(request)
        content = response.read()
        if (content):
            try:
                return json.loads(content)['words_result'][0]['words']
            except:
                print '识别文字错误！'
                return ''
        else:
            return ''


if __name__ == '__main__':
    API_KEY = 'XXXXXXXXXXXXXXXXXXXX'
    SECRET_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXX'
    IMG = 'D:\home_count_1.png'
    ocr = BaiduAIOCR(API_KEY,SECRET_KEY)
    access_token = ocr.get_access_token()
    text = ocr.do_recognition(access_token,IMG)
    print text
