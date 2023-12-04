import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

o = cv.imread('../water_coins.jpg',cv.IMREAD_UNCHANGED)
gray = cv.cvtColor(o,cv.COLOR_BGR2GRAY)
img = cv.cvtColor(o,cv.COLOR_BGR2RGB)
ishow = img.copy()
k = np.ones((5,5),np.uint8)
print(k)
e = cv.erode(o,k)
b = cv.subtract(o,e)

ret, thresh = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
kernel = np.ones((3,3), np.uint8)
opening = cv.morphologyEx(thresh,cv.MORPH_OPEN,kernel,iterations=2)

dis_transform = cv.distanceTransform(opening,cv.DIST_L2,5)
ret,fore = cv.threshold(dis_transform,0.7*dis_transform.max(),255,0)
plt.subplot(231),plt.imshow(o),plt.axis('off')
plt.subplot(232),plt.imshow(e),plt.axis('off')
plt.subplot(233),plt.imshow(b),plt.axis('off')
plt.subplot(234),plt.imshow(dis_transform),plt.axis('off')
plt.subplot(235),plt.imshow(fore),plt.axis('off')
plt.show()

