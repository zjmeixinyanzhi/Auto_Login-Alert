#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PIL import Image,ImageEnhance
from bs4 import BeautifulSoup
from baidu_ai_ocr import BaiduAIOCR

def do_login():
    # 加载Chrome浏览器驱动，打开网页
    driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver_win32\chromedriver.exe')
    driver.set_window_size(1302, 923)
    driver.get("XXXXXXXXXXXXXX")

    # 验证码图片截图，注意截图框的坐标
    snap_image = 'D:\shotsnap.png'
    code_image = 'D:\image_code.png'
    driver.get_screenshot_as_file(snap_image)
    im = Image.open(snap_image)
    box = (1265, 470, 1371, 505)
    region = im.crop(box)
    region.save(code_image)

    # 识别验证码
    API_KEY = 'XXXXXXXXXXXXXXXX'
    SECRET_KEY = 'XXXXXXXXXXXXXXX'
    ocr = BaiduAIOCR(API_KEY, SECRET_KEY)
    access_token = ocr.get_access_token()
    if access_token is '':
        exit()
    code = ocr.do_recognition(access_token, code_image)
    print code

    # 登录页面
    elem_user = driver.find_element_by_id("tbxUserName")
    elem_user.send_keys("XXXXXXXXXXX")
    elem_pwd = driver.find_element_by_id("tbxPassword")
    elem_pwd.send_keys("XXXXXXXXXXXXX")
    elem_verify_code = driver.find_element_by_id("tbxCaptcha")
    elem_verify_code.send_keys(code)
    elem_pwd.send_keys(Keys.RETURN)

    # 解析html
    html_doc = driver.page_source
    # print html_doc
    soup = BeautifulSoup(html_doc, 'lxml')
    links = soup.find_all('a')
    links = soup.find_all('span', { 'class' : 'count_item'})
    for link in links:
        #check_alert(link)
        print link
    time.sleep(5)
    driver.quit()

if __name__ == '__main__':
    do_login()