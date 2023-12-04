import cv2 as cv
import numpy as np

lena = cv.imread('../lena.jpg', 0)
cv.imshow('lena', lena)
r, c = lena.shape
x = np.zeros((r, c, 8), dtype=np.uint8)
for i in range(8):
    x[:, :, i] = 2**i
r = np.zeros((r, c, 8), dtype=np.uint8)
for i in range(8):
    # 位平面提取
    r[:, :, i] = cv.bitwise_and(lena, x[:, :, i])
    # 把当前平面大于0的设置为true 0 为黑色
    mask = r[:, :, i] > 0
    # 将白色赋值到true的坐标
    r[mask] = 255
    # 除了黑色的其他的会变白
    cv.imshow(str(i), r[:, :, i])
cv.waitKey()
cv.destroyAllWindows()
