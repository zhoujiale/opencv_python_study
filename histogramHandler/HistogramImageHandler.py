import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

lena = cv.imread('../lena.jpg',cv.IMREAD_GRAYSCALE)

cv.imshow('lena',lena)
histb = cv.calcHist([lena],[0],None,[256],[0,255])
mask = np.zeros(lena.shape,np.uint8)
mask[170:340,180:350] = 255
histM = cv.calcHist([lena],[0],mask,[256],[0,255])
print(lena.shape)
plt.plot(histb,color='b')
plt.plot(histM,color='r')
plt.show()
cv.waitKey()
cv.destroyAllWindows()

