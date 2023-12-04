import cv2 as cv

lena = cv.imread('../lena.jpg')
print(lena.shape)
print('==========================================')
data = lena.reshape((-1,3))
print(data.shape)

print(type('1.8'))