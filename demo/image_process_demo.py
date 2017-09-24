#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys
from PIL import Image,ImageDraw,ImageFont,ImageFilter

origin_img = 'D:/tiger.bmp'
blur_img = 'D:/tmp.bmp'
im = Image.open(origin_img)

im1 = im.filter(ImageFilter.BLUR)
im1.show()
im1.save(blur_img)
im2 = im.transpose(Image.ROTATE_270)
im2.show()
im.close()

