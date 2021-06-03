# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 9:20
# @Author  : Guoji
# @Email   : Guojinjia0729@Gmail.com
# @File    : question13.py

import cv2
import numpy as np


def BGR2GRAY(img):
    b = img[:, :, 0].copy()
    g = img[:, :, 1].copy()
    r = img[:, :, 2].copy()

    out = (0.2126 * r + 0.7152 * g + 0.0722 * b).astype(np.uint8)

    return out


def max_min_filter(img, g=3):
    gray = img.copy()

    x, y = gray.shape
    pad = np.zeros((x+2, y+2))
    pad[1:x+1, 1:y+1] = gray

    p, q = pad.shape
    out = pad.copy()
    for i in range(p-g+1):
        for j in range(q-g+1):
                out[i+1, j+1] = np.max(pad[i:i+g, j:j+g])- np.min(pad[i:i+g, j:j+g])

    out = out[1:p-1, 1:q-1].astype(np.uint8)

    return out

img = cv2.imread(r'C:\Users\Guoji\Desktop\FUCK_THE_WORLD\co_op\second_intern\ImageProcessing100Wen-master\Question_11_20\imori.jpg')
gray = BGR2GRAY(img)
out = max_min_filter(gray)
cv2.imshow('out', out)

cv2.waitKey()















