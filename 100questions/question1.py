# -*- coding: utf-8 -*-
# @Time    : 2021/5/21 10:39
# @Author  : Guoji
# @Email   : Guojinjia0729@Gmail.com
# @File    : question1.py

import cv2

aim = cv2.imread(r'C:\Users\Guoji\Desktop\FUCK_THE_WORLD\co_op\second_intern\ImageProcessing100Wen-master\Question_01_10\imori.jpg',1)
img = aim.copy()

blue = img[:, :, 0]
green = img[:, :, 1]
red = img[:, :, 2]

aim[:, :, 0] = red
aim[:, :, 2] = blue

cv2.imshow('aim', aim)
cv2.imshow('img', img)

cv2.waitKey()

