import cv2 as cv
lena = cv.imread('../lena.jpg',cv.IMREAD_GRAYSCALE)
r1 = cv.Canny(lena,128,200)
r2 = cv.Canny(lena,32,128)

cv.imshow('lena',lena)
cv.imshow('r1',r1)
cv.imshow('r2',r2)
cv.waitKey()
cv.destroyAllWindows()