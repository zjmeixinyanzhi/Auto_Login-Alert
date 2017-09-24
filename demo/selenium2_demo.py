#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver_win32\chromedriver.exe')
driver.set_window_size(1024, 768)
driver.get('http://zjzone.cc')

elem_firt_post = driver.find_element_by_class_name('post-title')
elem_firt_post.click()

elem_search = driver.find_element_by_id('s')
elem_search.send_keys('openstack')
elem_search.send_keys(Keys.RETURN)

time.sleep(50)
driver.close()