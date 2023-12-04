import cv2 as cv
import numpy as np

lena = cv.imread('../lena.jpg', 0)
mark = cv.imread('../mark.jpg', 0)
cv.imshow('mark', mark)
watermark = cv.resize(mark, (532, 528))
print(watermark)
w = watermark[:, :] > 0
watermark[w] = 1
r = lena.shape[0]
c = lena.shape[1]
# 嵌入
t254 = np.ones((r, c), dtype=np.uint8)*254
lenaH7 = cv.bitwise_and(lena, t254)
e = cv.bitwise_or(lenaH7, watermark)

# 提取
t1 = np.ones((r, c), dtype=np.uint8)
wm = cv.bitwise_and(e, t1)
# print(wm)

w = wm[:, :] > 0
wm[w] = 255

cv.imshow('lena', lena)
cv.imshow('watermark', watermark*255)
cv.imshow('e', e)
cv.imshow('wm', wm)
cv.waitKey()
cv.destroyAllWindows()
