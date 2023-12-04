import cv2 as cv
import numpy as np

src = cv.imread('../lena.jpg',cv.IMREAD_GRAYSCALE)

scharrx = cv.Scharr(src,cv.CV_64F,1,0)
scharrx_result = cv.convertScaleAbs(scharrx)
scharry = cv.Scharr(src,cv.CV_64F,0,1)
scharry_result = cv.convertScaleAbs(scharry)
scharrxy_result = cv.addWeighted(scharrx_result,0.5,scharry_result,0.5,0)
cv.imshow('src',src)
cv.imshow('x',scharrx_result)
cv.imshow('y',scharry_result)
cv.imshow('xy',scharrxy_result)
cv.waitKey()
cv.destroyAllWindows()