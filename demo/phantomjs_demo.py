#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from PIL import Image
from selenium.webdriver.common.keys import Keys

driver = webdriver.PhantomJS()
driver.set_window_size(1024, 768)
driver.get('http://zjzone.cc')

snap_image = 'D:\shotsnap.png'
driver.get_screenshot_as_file(snap_image)
im = Image.open(snap_image)
im.show()

time.sleep(50)
driver.close()