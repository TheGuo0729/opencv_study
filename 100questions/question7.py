# -*- coding: utf-8 -*-
# @Time    : 2021/5/28 15:10
# @Author  : Guoji
# @Email   : Guojinjia0729@Gmail.com
# @File    : question7.py

import cv2
import numpy as np


def averagepooling_8(img):
    x, y, z = img.shape
    out = img.copy()
    x_move = int(x/8)
    y_move = int(y/8)
    for i in range(x_move):
        for j in range(y_move):
            for k in range(z):
                out[8 * j:8 * (j+1), 8 * i:8 * (i+1), k] = np.mean(out[8 * j:8 * (j+1), 8 * i:8 * (i+1), k])
                # out[8 * j:8 * (j+1), 8 * i:8 * (i+1), k] = np.max(out[8 * j:8 * (j+1), 8 * i:8 * (i+1), k]) ....问题⑧
    out = out.astype(np.uint8)
    return out


img = cv2.imread(r'C:\Users\Guoji\Desktop\FUCK_THE_WORLD\co_op\second_intern\ImageProcessing100Wen-master\Question_01_10\imori.jpg')
out = averagepooling_8(img)
cv2.imshow('out', out)
cv2.waitKey()

