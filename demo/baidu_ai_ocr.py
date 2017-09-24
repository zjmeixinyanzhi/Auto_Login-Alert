#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib, urllib2, sys, base64
import ssl
import json

API_KEY = 'XXXXXXXXXXXXXXXXXXXXXX'
SECRET_KEY = 'XXXXXXXXXXXXXXXXXXXXXX'

def get_access_token():
    '''获取access_token'''
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' \
       +API_KEY+ '&client_secret=' + SECRET_KEY
    request = urllib2.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib2.urlopen(request)
    content = response.read()
    if (content):
        return json.loads(content)['access_token']
    else:
        return ''

def get_verification_code(access_token, image_path):
    '获取百度AI识别的验证码'
    url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general?access_token=' + access_token
    # 二进制方式打开图文件
    f = open(image_path,'rb')
    # 参数image：图像base64编码
    img = base64.b64encode(f.read())
    params = {"image": img}
    params = urllib.urlencode(params)
    request = urllib2.Request(url, params)
    request.add_header('Content-Type', 'application/x-www-form-urlencoded')
    response = urllib2.urlopen(request)
    content = response.read()
    if (content):
        return json.loads(content)['words_result'][0]['words']
    else:
        return ''

if __name__ == '__main__':
    code_image = 'D:\image_code.png'
    access_token = get_access_token()
    code = get_verification_code(access_token, code_image)
    print code