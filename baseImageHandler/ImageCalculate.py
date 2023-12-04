import cv2 as cv
import numpy as np

# 图像加法
a = cv.imread('../lena.jpg')
b = a
'''+ 运算 a+b 小于等于255结果不变；大于255，对255求余数作为结果'''
result1 = a + b
'''add 运算 a+b 小于等于255结果不变；大于255结果为255'''
result2 = cv.add(a, b)
# cv.imshow('original', a)
# cv.imshow('result1',result1)
# cv.imshow('result2',result2)

# 图像加权和
img1 = np.ones(shape=(3, 4), dtype=np.uint8) * 100
img2 = np.ones(shape=(3, 4), dtype=np.uint8) * 10
gamma = 3
# src1 * alpha +  src2 * beta + gamma *** 图像大小需要一致
img3 = cv.addWeighted(img1, 0.6, img2, 5, gamma=gamma)

print(img1)
print(img2)
print(img3)

boat = cv.imread('../boat.jpeg')
boat_change = cv.resize(boat, dsize=(532, 528))
cv.imshow('boat', boat_change)
lena = cv.imread('../lena.jpg')
cv.imshow('lena', lena)
result = cv.addWeighted(lena, 0.6, boat_change, 0.4, 0)
cv.imshow('result', result)

cv.waitKey()
cv.destroyAllWindows()
