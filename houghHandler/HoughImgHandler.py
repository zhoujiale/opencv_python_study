import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('../computer.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray,50,150,apertureSize=3)
orgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
oShow = orgb.copy()
lines = cv.HoughLines(edges,1,np.pi/180,140)
for line in lines:
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv.line(orgb, (x1,y1),(x2,y2),(0,0,255),2)

plt.subplot(121),plt.imshow(oShow),plt.axis('off')
plt.subplot(122),plt.imshow(orgb),plt.axis('off')
plt.show()