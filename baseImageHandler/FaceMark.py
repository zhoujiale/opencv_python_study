import cv2 as cv
import numpy as np

# 获取单通道灰度图
lena = cv.imread('../lena.jpg', 0)
# 获取 行列
r, c = lena.shape
# 获取一个全0矩阵
mask = np.zeros((r, c), dtype=np.uint8)
# 标记脸部范围
mask[220:400, 250:350] = 1
# 随机一个雪花图
key = np.random.randint(0, 256, size=[r, c], dtype=np.uint8)
# 加密原图
lenaXorKey = cv.bitwise_xor(lena, key)
# 获取加密的脸部 *255 二值转灰度
encryptFace = cv.bitwise_and(lenaXorKey, mask*255)
# 1-mask相当于取反，黑白颠倒，原来的脸部白色变黑
noFace1 = cv.bitwise_and(lena, (1-mask)*255)
# 图像加法
maskFace = encryptFace+noFace1
# 获取原图
extractOriginal = cv.bitwise_xor(maskFace, key)
extractFace = cv.bitwise_and(extractOriginal, mask*255)
noFace2 = cv.bitwise_and(maskFace, (1-mask)*255)
extractLena = noFace2+extractFace
cv.imshow("lena", lena)
cv.imshow("mask", mask*255)
cv.imshow("1-mask", (1-mask)*255)
cv.imshow("key", key)
cv.imshow("lenaXorKey", lenaXorKey)
cv.imshow("encryptFace", encryptFace)
cv.imshow("noFace1", noFace1)
cv.imshow("maskFace", maskFace)
cv.imshow("extractOriginal", extractOriginal)
cv.imshow("extractFace", extractFace)
cv.imshow("noFace2", noFace2)
cv.imshow("extractLena", extractLena)
cv.waitKey()
cv.destroyAllWindows()
