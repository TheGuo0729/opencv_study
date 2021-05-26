# -*- coding: utf-8 -*-
# @Time    : 2021/5/26 9:59
# @Author  : Guoji
# @Email   : Guojinjia0729@Gmail.com
# @File    : question4.py

#大津二值化算法

import cv2
import numpy as np

aim = cv2.imread(r'C:\Users\Guoji\Desktop\FUCK_THE_WORLD\co_op\second_intern\ImageProcessing100Wen-master\Question_01_10\imori.jpg', 0)


def dajinerzhihua(img):
    x, y = img.shape
    total = x * y
    ls = []
    t = 0
    while t < 256:
        n_1 = len(np.where(img > t))
        w = n_1/total
        m_0 = np.mean(np.where(img > t, img, 0))
        m_1 = np.mean(np.where(img > t, 0, img))
        c = w * (1 - w) * (m_0 - m_1)**2
        ls.append(c)
        t = t+ 1
    th = 255 - ls.index(min(ls))
    img_out = np.where(img < th, 0, 255)
    img_out = np.array(img_out, dtype=np.uint8)
    cv2.imshow('out', img_out)
    cv2.waitKey()


dajinerzhihua(aim)

