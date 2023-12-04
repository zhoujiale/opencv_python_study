import cv2 as cv
import numpy as np

img=np.random.randint(0,256,size=[256,256],dtype=np.uint8)
cv.imshow("demo",img)
lena = cv.imread('../lena.jpg')
b,g,r = cv.split(lena)
cv.imshow("B",b)
cv.imshow("G",g)
cv.imshow("R",r)
cv.waitKey()
cv.destroyAllWindows()