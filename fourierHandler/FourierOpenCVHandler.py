import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

lena = cv.imread('../lena.jpg',0)
dft = cv.dft(np.float32(lena),flags=cv.DFT_COMPLEX_OUTPUT)
dftShift = np.fft.fftshift(dft)
result = 20*np.log(cv.magnitude(dftShift[:,:,0],dftShift[:,:,1]))
plt.subplot(121),plt.imshow(lena,cmap='gray')
plt.title('original'),plt.axis('off')
plt.subplot(122),plt.imshow(result,cmap='gray')
plt.title('result'),plt.axis('off')
plt.show()