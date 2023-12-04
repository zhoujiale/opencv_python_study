import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

rand1 = np.random.randint(0,30,(20,2)).astype(np.float32)
rand2 = np.random.randint(70,100,(20,2)).astype(np.float32)

trainData = np.vstack((rand1, rand2))

r1Label = np.zeros((20,1)).astype(np.float32)
r2Label = np.ones((20,1)).astype(np.float32)
tdLable = np.vstack((r1Label,r2Label))
print(tdLable)
g = trainData[tdLable.ravel() == 0]
plt.scatter(g[:,0],g[:,1],80,'g','o')
b = trainData[tdLable.ravel() == 1]
plt.scatter(b[:,0],b[:,1],80,'b','s')
test = np.random.randint(0,100,(1,2)).astype(np.float32)
plt.scatter(test[:,0],test[:,1],80,'r','*')

knn = cv.ml.KNearest_create()
knn.train(trainData, cv.ml.ROW_SAMPLE, tdLable)
ret, results, neighbours, dist = knn.findNearest(test, 5)

print('类型:',results)
print('距离最近的是:', neighbours)
print('最近距离:', dist)
plt.show()