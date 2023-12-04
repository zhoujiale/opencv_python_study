import cv2 as cv
import numpy as np

lena = cv.imread('../lena.jpg',0)
# 椒盐噪声的数目比例
s_vc_p = 0.5
# 添加噪声图像像素的数目
amount = 0.04
noisy_img = np.copy(lena)
# 添加噪声
num_salt = np.ceil(amount * lena.size * s_vc_p)
# 设置噪声坐标
coords = [np.random.randint(0, i - 1, int(num_salt)) for i in lena.shape]
noisy_img[coords] = 255
# 添加噪声
num_pepper = np.ceil(amount * lena.size * (1. - s_vc_p))
# 设置添加噪声的位置
coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in lena.shape]
noisy_img[coords] = 0
img2 = np.hstack([lena, noisy_img])
cv.imshow('lena', lena)
cv.imshow('noise', img2)
cv.waitKey()
cv.destroyAllWindows()
