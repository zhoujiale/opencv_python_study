import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

boat = cv.imread('../boat.jpeg',0)
f = np.fft.fft2(boat)
fshift = np.fft.fftshift(f)

rows, cols = boat.shape
crow,ccol = int(rows/2), int(cols/2)

fshift[crow-30:crow+30,ccol-30:ccol+30]=0
ishift = np.fft.ifftshift(fshift)
iimg = np.fft.ifft2(ishift)
iimg = np.abs(iimg)

plt.subplot(121),plt.imshow(boat,cmap= 'gray')
plt.title('original'),plt.axis('off')
plt.subplot(122),plt.imshow(iimg,cmap='gray')
plt.title('result'),plt.axis('off')
plt.show()
