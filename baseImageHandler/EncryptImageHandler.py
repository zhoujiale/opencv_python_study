import cv2 as cv
import numpy as np

lena = cv.imread('../lena.jpg', 0)
r = lena.shape[0]
c = lena.shape[1]
print(lena.shape)
key = np.random.randint(0, 256, size=[r, c], dtype=np.uint8)
print(key.shape)
# 异或操作加密
encryption = cv.bitwise_xor(lena, key)

cv.imshow('lena', lena)
cv.imshow('key', key)
cv.imshow('encrypt', encryption)

decryption = cv.bitwise_xor(encryption, key)

cv.imshow('decrypt', decryption)
cv.waitKey()
cv.destroyAllWindows()
