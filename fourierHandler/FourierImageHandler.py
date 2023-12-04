import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

lena = cv.imread('../lena.jpg',0)
f = np.fft.fft2(lena)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))
plt.subplot(121)
plt.imshow(lena,cmap='gray')
plt.title('original')
plt.axis('off')
plt.subplot(122)
plt.imshow(magnitude_spectrum,cmap='gray')
plt.title('result')
plt.axis('off')
plt.show()