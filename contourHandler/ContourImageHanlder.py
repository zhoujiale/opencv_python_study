import cv2 as cv
import numpy as np

flower = cv.imread('../flower.jpg')
cv.imshow('original', flower)
# 转灰度
gray = cv.cvtColor(flower, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
# 阈值分割
ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
cv.imshow('binary',binary)
#注意opencv 4中返回值只有两个
contours, hierarchy = cv.findContours(
    binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
mask = np.zeros(flower.shape,np.uint8)    
mask = cv.drawContours(mask,contours,-1,(255,255,255,255),-1)

cv.imshow('mask',mask)
loc = cv.bitwise_and(flower,mask)
cv.imshow('loc',loc)
cv.waitKey()
cv.destroyAllWindows()
