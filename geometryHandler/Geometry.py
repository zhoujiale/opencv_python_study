import cv2 as cv
import numpy as np

img = cv.imread('../lena.jpg')
rows = img.shape[0]
cols = img.shape[1]
ch = img.shape[2]
p1 = np.float32([[0, 0], [cols-1, 0], [0, rows-1]])
p2 = np.float32(
    [[0, rows*0.33], [cols*0.85, rows*0.25], [cols*0.15, rows*0.7]])
M = cv.getAffineTransform(p1, p2)
dst = cv.warpAffine(img, M, (cols, rows))
cv.imshow('lena', img)
cv.imshow('result', dst)
cv.waitKey()
cv.destroyAllWindows()
