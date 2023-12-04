import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

lena = cv.imread('../lena.jpg',0)
template = cv.imread('../lena_match.png',0)

th, tw = template.shape[::]
rv = cv.matchTemplate(lena,template,cv.TM_SQDIFF)
minVal,maxVal,minLoc,maxLoc = cv.minMaxLoc(rv)

topLeft = minLoc
bottomRight = (topLeft[0] + tw,topLeft[1]+th)
cv.rectangle(lena,topLeft,bottomRight,255,2)
plt.subplot(121), plt.imshow(lena,cmap='gray')
plt.title('lena'),plt.axis('off')
plt.subplot(122), plt.imshow(rv,cmap='gray')
plt.title('rv'),plt.axis('off')
plt.show()