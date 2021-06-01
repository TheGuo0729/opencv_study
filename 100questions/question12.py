# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 17:11
# @Author  : Guoji
# @Email   : Guojinjia0729@Gmail.com
# @File    : question12.py

import cv2
import numpy as np


def MotionFilter(img, s=3):
    x, y, z = img.shape
    out = img.copy()
    ker = np.array([[1/3, 0, 0], [0, 1/3, 0], [0, 0, 1/3]])
    p = np.zeros((x+2, y+2, 3))
    p[1:x+1, 1:y+1] = out


    for i in range(x-s+1):
        for j in range(y-s+1):
            for k in range(z):
                out[i+1, j+1, k] =np.sum(ker * img[i:i+s, j:j+s, k])
    return out


img = cv2.imread(r'C:\Users\Guoji\Desktop\FUCK_THE_WORLD\co_op\second_intern\ImageProcessing100Wen-master\Question_01_10\imori.jpg')
out = MotionFilter(img)
cv2.imshow('img', out)
cv2.waitKey()
