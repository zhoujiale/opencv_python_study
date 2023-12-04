import cv2 as cv
lena = cv.imread('../lena.jpg')
rgb = cv.cvtColor(lena, cv.COLOR_BGR2RGB)
cv.imshow('lena', lena)
cv.imshow('rgb', rgb)
cv.waitKey()
cv.destroyAllWindows()
