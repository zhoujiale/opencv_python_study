import cv2 as cv

lena = cv.imread('../lena.jpg',cv.IMREAD_GRAYSCALE)

result1 = cv.pyrDown(lena)
result2 = cv.pyrDown(result1)
result3 = cv.pyrDown(result2)

g = lena

g1 = cv.pyrDown(g)

l = g - cv.pyrUp(g1)
g2 = cv.pyrUp(g1)
r = l + cv.pyrUp(g1)

print("lena.shape=",lena.shape)
print("result1.shape=",result1.shape)

cv.imshow('lena',lena)
cv.imshow('result1',result1)
cv.imshow('r',r)
cv.imshow('g2',g2)
cv.waitKey()
cv.destroyAllWindows()