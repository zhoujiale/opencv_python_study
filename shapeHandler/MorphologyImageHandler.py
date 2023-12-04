import cv2 as cv
import numpy as np

src = cv.imread('../ercode.png',cv.IMREAD_UNCHANGED)
k = np.ones((7,7),np.uint8)
# 开操作  去除毛刺噪声
result = cv.morphologyEx(src,cv.MORPH_OPEN,k)
# 梯度操作
result2 = cv.morphologyEx(src,cv.MORPH_GRADIENT,k)
# 礼帽运算 获取图形外部噪声
result3 = cv.morphologyEx(src,cv.MORPH_TOPHAT,k)
# 黑帽运算 获取图形内部的小孔
result4 = cv.morphologyEx(src,cv.MORPH_BLACKHAT,k)
cv.imshow('src',src)
cv.imshow('result',result)
cv.imshow('result2',result2)
cv.imshow('result3',result3)
cv.imshow('result4',result4)
cv.waitKey()
cv.destroyAllWindows()