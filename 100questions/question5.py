# -*- coding: utf-8 -*-
# @Time    : 2021/5/26 11:06
# @Author  : Guoji
# @Email   : Guojinjia0729@Gmail.com
# @File    : question5.py

# HSV 色彩变换
import cv2
import numpy as np


def rgb2hsv(img):
    img_1 = img.copy() / 255
    max_i = np.max(img_1, axis=2).copy()
    min_i = np.min(img_1, axis=2).copy()
    h = np.zeros_like(img)

    ind_1 = np.where(min_i == img_1[..., 0])
    ind_2 = np.where(min_i == img_1[..., 2])
    ind_3 = np.where(min_i == img_1[..., 1])

    h[..., 0][np.where(max_i == min_i)] = 0
    h[..., 0][ind_1] = 60 * ((img_1[..., 1][ind_1] - img_1[..., 2][ind_1]) / (max_i[ind_1] - min_i[ind_1])) + 60
    h[..., 0][ind_2] = 60 * ((img_1[..., 0][ind_2] - img_1[..., 1][ind_2]) / (max_i[ind_2] - min_i[ind_2])) + 180
    h[..., 0][ind_3] = 60 * ((img_1[..., 2][ind_3] - img_1[..., 0][ind_3]) / (max_i[ind_3] - min_i[ind_3])) + 300

    h[..., 1] = max_i.copy() - min_i.copy()
    h[..., 2] = max_i.copy()

    return h


def hsv2bgr(img, h):
    img_1 = img.copy() / 255
    max_i = np.max(img_1, axis=2).copy()
    min_i = np.min(img_1, axis=2).copy()

    c = h[..., 1]
    h_1 = (h[..., 0]) / 60
    h_2 = h[..., 0]
    x = c * (1 - np.abs(h_1 % 2 - 1))
    all_zeros = np.zeros_like(h_2)

    out = np.zeros_like(img)

    "mat = [[c, x, all_zeros], [x, c, all_zeros], [all_zeros, c, x], [all_zeros, x, c], [x, all_zeros, c],[c, all_zeros, x]]"
    mat = [[all_zeros, x, c], [all_zeros, c, x], [x, c, all_zeros], [c, x, all_zeros], [c, all_zeros, x],
           [x, all_zeros, c]]
    '注意顺序的转化，原本我的顺序是按照原理里面的顺序但实际图像输出时，B，R通道需要调换一下顺序，所以mat里面的顺序需要修改一下'
    for i in range(6):
        ind = np.where((h_1 >= i) & (h_1 < (i + 1)))
        out[..., 0][ind] = (h[..., 2] - h[..., 1])[ind] + mat[i][0][ind]
        out[..., 1][ind] = (h[..., 2] - h[..., 1])[ind] + mat[i][1][ind]
        out[..., 2][ind] = (h[..., 2] - h[..., 1])[ind] + mat[i][2][ind]

    out[np.where(max_i == min_i)] = 0
    out = np.clip(out, 0, 1)
    out = (out * 255).astype(np.uint8)

    return out


img = cv2.imread(
    r'C:\Users\Guoji\Desktop\FUCK_THE_WORLD\co_op\second_intern\ImageProcessing100Wen-master\Question_01_10\imori.jpg').astype(
    np.float32)

h = rgb2hsv(img)

h[..., 0] = (h[..., 0] + 180) % 360

out = hsv2bgr(img, h)

cv2.imwrite("out_bgr.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()





