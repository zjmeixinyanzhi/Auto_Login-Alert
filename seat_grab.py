#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib,urllib2,sys,base64
import ssl,json,time,datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PIL import Image,ImageEnhance
from bs4 import BeautifulSoup
import smail

driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver_win32\chromedriver.exe')
driver.set_window_size(1024, 768)
driver.get('http://202.194.143.47/Home/Web/floor/area/20')

elem_login = driver.find_element_by_class_name('login-btn')
elem_login.click()
elem_user = driver.find_element_by_name('username')
elem_user.send_keys('XXXXXXXXXXXXXXXXX')
elem_pwd = driver.find_element_by_name('password')
elem_pwd.send_keys('XXXXXXXXXXXXXX')

# 验证码图片截图，注意截图框的坐标
snap_image = 'D:\shotsnap.png'
code_image = 'D:\image_code.png'
driver.get_screenshot_as_file(snap_image)
im = Image.open(snap_image)
box = (667, 387, 771, 443)
region = im.crop(box)
#region.show()
region.save(code_image)

# 登录
text = raw_input('请手动输入验证码：')
elem_verify_code = driver.find_element_by_name('verify')
elem_verify_code.send_keys(text)
elem_confirm = driver.find_element_by_xpath('/html/body/div[4]/div/table/tbody/tr[3]/td/div[2]/button[2]')
elem_confirm.click()
time.sleep(5)

is_wait = True
i = datetime.datetime.now()
d1 = datetime.datetime.now()
d3 = d1 + datetime.timedelta(days=2)
tomorrow = d3.date()

img1 = 'D:\snap001.png'
img2 = 'D:\snap002.png'

# 动态链接
dynamic_url = 'http://202.194.143.47/Home/Web/area?area=29&segment=1423123&day=' + str(tomorrow) + '&startTime=08:00&endTime=21:50'
num = 39
while is_wait:
    if i.hour != 0:
        '''抢着玩，防止退出登录'''
        driver.get(dynamic_url)
        time.sleep(3)
        try:
            elem_curr = driver.find_element_by_xpath('/html/body/div/ul/li[' + str(num) + ']')
            elem_curr.click()
            elem_confirm = driver.find_element_by_class_name('ui-dialog-autofocus')
            time.sleep(5)
            elem_confirm.click()
        except:
            print 'error'
        i = datetime.datetime.now()
        print datetime.datetime.now()
    elif i.hour == 0 and i.minute >= 0:
        '''抢占'''
        print '\n开始抢占'+ str(tomorrow) + '的座位'
        driver.get(dynamic_url)
        time.sleep(3)
        # 获取
        optimal_list = [39, 40, 38, 37, 43, 44, 45, 46, 47]
        for num in optimal_list:
            '''按照优先级抢占'''
            print '>', num
            elem_curr = driver.find_element_by_xpath('/html/body/div/ul/li[' + str(num) + ']')
            elem_curr.click()
            time.sleep(2)
            elem_confirm = driver.find_element_by_xpath(
                '/html/body/div[3]/div/table/tbody/tr[3]/td/div[2]/button[2]')
            elem_confirm.click()
            driver.save_screenshot(img1)
            time.sleep(5)
            # 检查是否抢占成功
            elem_info_center = driver.find_element_by_class_name('login-welcome')
            elem_info_center.click()
            time.sleep(2)
            main_window = driver.current_window_handle
            driver.switch_to.window(driver.window_handles[1])
            driver.save_screenshot(img2)
            info_doc = driver.page_source
            soup = BeautifulSoup(info_doc, 'lxml')
            table = soup.find_all('tbody')[0]
            tr = table.find_all('tr')[0]
            tds = tr.find_all('td')
            result = str(tr)
            if result.__contains__(str(tomorrow)) and result.__contains__('预约成功'):
                '''发送邮件通知'''
                print 'alert'
                smail.send_mail()
                is_wait = False
                break
            driver.close()
            driver.switch_to.window(main_window)
