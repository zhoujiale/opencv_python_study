import cv2 as cv
import numpy as np

blue = np.zeros((300,300,3),dtype=np.uint8)
blue[:,:,0]=255
cv.imshow('blue',blue)

green = np.zeros((300,300,3),dtype=np.uint8)
green[:,:,1]=255
cv.imshow('green',green)

red = np.zeros((300,300,3),dtype=np.uint8)
red[:,:,2]=255
cv.imshow('red',red)
cv.waitKey()
cv.destroyAllWindows()