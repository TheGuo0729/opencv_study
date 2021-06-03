# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 14:50
# @Author  : Guoji
# @Email   : Guojinjia0729@Gmail.com
# @File    : question14.py

import cv2
import numpy as np

def Differential_folter(img, s=3):
    x, y = img.shape
    padding = np.zeros((x+2, y+2))
    padding[1:x+1, 1:y+1] = img
    out_1 = padding.copy()
    out_2 = padding.copy()

    k_x = np.array([[0, -1, 0], [0, 1, 0], [0, 0, 0]])
    k_y = np.array([[0, 0, 0], [-1, 1, 0], [0, 0, 0]])

    #k_x = np.array([[1, 2. 1], [0, 0, 0], [-1, -2, -1]])
    #k_y = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])  这是Sobel算子

    #k_x = np.array([[-1, -1. -1], [0, 0, 0], [1, 1, 1]])
    #k_y = np.array([[-1, 0, -1], [-1, 0, 1], [-1, 0, 1]])  这是Prewitt滤波器

    p, q = padding.shape
    for i in range(p-s+1):
        for j in range(q-s+1):
            out_1[i+1, j+1] = np.sum(padding[i:i+s, j:j+s] * k_x)
            out_2[i+1, j+1] = np.sum(padding[i:i+s, j:j+s] * k_y)

    out_1 = np.clip(out_1, 0, 255)
    out_2 = np.clip(out_2, 0, 255)

    out_1 = out_1[1:p-1, 1:q-1].astype(np.uint8)
    out_2 = out_2[1:p-1, 1:q-1].astype(np.uint8)
    return out_1, out_2


img = cv2.imread(r'C:\Users\Guoji\Desktop\FUCK_THE_WORLD\co_op\second_intern\ImageProcessing100Wen-master\Question_11_20\imori.jpg')
gray = BGR2GRAY(img)
out_1, out_2 = Differential_folter(gray)

cv2.imshow('out_x', out_1)
cv2.imshow('out_y', out_2)
cv2.waitKey()
