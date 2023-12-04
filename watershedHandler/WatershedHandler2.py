import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('../water_coins.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
ishow=img.copy()
ret, thresh = cv.threshold(gray,0,255,
cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
kernel = np.ones((3,3),np.uint8)
opening = cv.morphologyEx(thresh,cv.MORPH_OPEN,kernel, iterations = 2)
sure_bg = cv.dilate(opening,kernel,iterations=3)
dist_transform = cv.distanceTransform(opening,cv.DIST_L2,5)
ret, fore = cv.threshold(dist_transform,0.7*dist_transform.max(),255,0)
fore = np.uint8(fore)
ret, markers1 = cv.connectedComponents(fore)
foreAdv=fore.copy()
unknown = cv.subtract(sure_bg,foreAdv)
ret, markers2 = cv.connectedComponents(foreAdv)
markers2 = markers2+1
markers2[unknown==255] = 0
plt.subplot(121)
plt.imshow(markers1)
plt.axis('off')
plt.subplot(122)
plt.imshow(markers2)
plt.axis('off')
plt.show()