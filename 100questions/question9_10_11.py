# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 11:39
# @Author  : Guoji
# @Email   : Guojinjia0729@Gmail.com
# @File    : question9.py

import cv2
import numpy as np

def GaussianFilter(img,K = 3):
    x, y, z = img.shape
    out = img.copy()
    ker = np.zeros((K, K, 3))
    p = np.zeros((x+2, y+2, 3))
    u, v, w = p.shape

    for i in range(1, u-1):
        for j in range(1, v-1):
            for k in range(w):
                p[i, j, k] = out[i-1, j-1, k]

#这是中值滤波
    for i in range(u-K):
        for j in range(v-K):
            for z in range(w):
                p[i+1, j+1, z] = np.median(p[i:i+K, j:j+K, z])
    p = p[1:u - 1, 1:v - 1].astype(np.uint8)
    return p
#将 26行中的 median 改为 mean 即为均值滤波

'''
这是高斯滤波
ker = np.array([[1/16, 2/16, 1/16], [2/16, 4/16, 2/16], [1/16, 2/16, 1/16]])

    for i in range(v-K+1):
        for j in range(u-K+1):
            for k in range(w):
                p[i+1, j+1, k] = np.sum(ker * p[i:i+K, j:j+K, k])
    p = p[1:u-1, 1:v-1].astype(np.uint8)
    return p
'''

img = cv2.imread(r'C:\Users\Guoji\Desktop\FUCK_THE_WORLD\co_op\second_intern\ImageProcessing100Wen-master\Question_01_10\imori_noise.jpg')
out = GaussianFilter(img)
cv2.imshow('img', out)
cv2.waitKey()
