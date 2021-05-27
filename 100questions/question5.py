# -*- coding: utf-8 -*-
# @Time    : 2021/5/26 11:06
# @Author  : Guoji
# @Email   : Guojinjia0729@Gmail.com
# @File    : question5.py

#HSV 色彩变换
import cv2
import numpy as np


def rgb2hsv(img):
    img_1 = img / 255
    max_i = np.max(img_1, axis=2)
    min_i = np.min(img_1, axis=2)
    h = np.zeros_like(img)

    ind_1 = np.where(min_i == img_1[..., 0])
    ind_2 = np.where(min_i == img_1[..., 2])
    ind_3 = np.where(min_i == img_1[..., 1])

    h[..., 0][np.where(max_i == min_i)] = 0
    h[..., 0][ind_1] = 60 * ((img[..., 1][ind_1] - img[..., 2][ind_1])/(max_i[ind_1] - min_i[ind_1])) + 60
    h[..., 0][ind_2] = 60 * ((img[..., 0][ind_2] - img[..., 1][ind_2])/(max_i[ind_2] - min_i[ind_2])) + 180
    h[..., 0][ind_3] = 60 * ((img[..., 2][ind_3] - img[..., 0][ind_3]) /(max_i[ind_3] - min_i[ind_3])) + 300

    h[..., 0] = (h[..., 0] + 180) % 360
    h[..., 1] = max_i - min_i
    h[..., 2] = max_i
    return h


def hsv2bgr(img, h):

    img_1 = img / 255
    max_i = np.max(img_1, axis=2)
    min_i = np.min(img_1, axis=2)

    c = h[..., 1]
    h_1 = h[..., 0]/60
    x = c * (1 - np.abs(h_1 % 2 - 1))
    all_zeros = np.zeros_like(h)
    out = np.zeros_like(h)
    mat = [[c, x, all_zeros], [x, c, all_zeros], [all_zeros, c, x], [all_zeros, x, c], [x, all_zeros, c], [c, all_zeros, x]]
    for i in range(6):
        ind = np.where((h_1 >= i) & (h_1 < (i+1)))
        out[..., 0][ind] = (h[..., 2] - c)[ind] + mat[i][0][ind]
        out[..., 1][ind] = (h[..., 2] - c)[ind] + mat[i][1][ind]
        out[..., 2][ind] = (h[..., 2] - c)[ind] + mat[i][2][ind]

    out[np.where(max_i == min_i)] = 0
    out = np.clip(out, 0, 1)
    out = (out * 255).astype(np.uint8)

    return out


img = cv2.imread(r'C:\Users\Guoji\Desktop\FUCK_THE_WORLD\co_op\second_intern\ImageProcessing100Wen-master\Question_01_10\imori.jpg').astype(np.float32)
#这个float32非常重要，但目前仍未明白float32，uint32，uint8的使用规则
h = rgb2hsv(img)

h[..., 0] = (h[..., 0] + 180) % 360

out = hsv2bgr(img, h)
cv2.imwrite("out_bgr.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()


