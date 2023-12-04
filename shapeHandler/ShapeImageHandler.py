import cv2 as cv
import numpy as np

ercode = cv.imread('../ercode.png',cv.IMREAD_UNCHANGED)
# 腐蚀 结构元
kernel = np.ones((9,9),np.uint8)
# 腐蚀操作
erosion = cv.erode(ercode,kernel=kernel,iterations=2)
cv.imshow('ercode',ercode)
cv.imshow('erosion',erosion)

dilation = cv.dilate(ercode,kernel=kernel)

cv.imshow('dilation',dilation)
cv.waitKey()
cv.destroyAllWindows()