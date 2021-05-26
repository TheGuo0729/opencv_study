# -*- coding: utf-8 -*-
# @Time    : 2021/5/21 11:05
# @Author  : Guoji
# @Email   : Guojinjia0729@Gmail.com
# @File    : question2.py

import cv2
import numpy as np

aim = cv2.imread(r'C:\Users\Guoji\Desktop\FUCK_THE_WORLD\co_op\second_intern\ImageProcessing100Wen-master\Question_01_10\imori.jpg',1)


blue = aim[:, :, 0]
green = aim[:, :, 1]
red = aim[:, :, 2]

img = aim.copy()

img[:, :, 0] = 0.0722 * blue
img[:, :, 1] = 0.7152 * green
img[:, :, 2] = 0.2126 * red

out = img[:, :, 0] + img[:, :, 1] + img[:, :, 2]
out = out.astype(np.uint8)

cv2.imwrite('out.jpg', out)
cv2.imshow('out', out)

c = 128
x, y = out.shape
for i in range(x):
    for j in range(y):
        if out[i][j] < c:
            out[i][j] = 0
        else:
            out[i][j] = 255

cv2.imwrite('1-0.jpg', out)
cv2.imshow('1-0', out)

cv2.waitKey()


