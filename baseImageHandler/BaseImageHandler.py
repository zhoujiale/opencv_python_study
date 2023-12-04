import cv2 as cv

# 读取图片
lena = cv.imread('../lena.jpg');
# print(lena)
# 创建窗口
# cv.namedWindow('lena')
cv.imshow('lena',lena)
# cv.waitKey(0)
retval = cv.imwrite('lena1.jpg',lena)
# print(retval)