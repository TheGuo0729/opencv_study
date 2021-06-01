# -*- coding: utf-8 -*-
# @Time    : 2021/5/27 15:59
# @Author  : Guoji
# @Email   : Guojinjia0729@Gmail.com
# @File    : question6.py

import cv2
import numpy as np


def secailianghua(img):
    img_1 = img.copy()
    img_1 = img_1 // 64 * 64 + 32
    return img_1


img = cv2.imread(r'C:\Users\Guoji\Desktop\FUCK_THE_WORLD\co_op\second_intern\ImageProcessing100Wen-master\Question_01_10\imori.jpg')
out = secailianghua(img)
cv2.imshow('img', out)

cv2.waitKey()


