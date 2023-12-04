import cv2 as cv
import numpy as np

src = cv.imread('../lena.jpg',0)
laplacian = cv.Laplacian(src,cv.CV_64F)
laplacian = cv.convertScaleAbs(laplacian)
cv.imshow('src',src)
cv.imshow('l',laplacian)
cv.waitKey()
cv.destroyAllWindows()