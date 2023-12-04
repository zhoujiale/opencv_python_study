import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

a = np.random.randint(95,100,(20,2)).astype(np.float32)
# print(a)
# print('------------------------------------')
b = np.random.randint(90,95,(20,2)).astype(np.float32)
data = np.vstack((a,b))
# print(data)
# print('-------------------------------------')
data = np.array(data,dtype='float32')

aLabel = np.zeros((20,1))
bLabel = np.ones((20,1))

label = np.vstack((aLabel,bLabel))
label = np.array(label,dtype='int32')
svm = cv.ml.SVM_create()
result = svm.train(data,cv.ml.ROW_SAMPLE,label)
print(result)
test = np.vstack([[98,90],[90,99]])
test = np.array(test,dtype='float32')
(p1,p2) = svm.predict(test)
plt.scatter(a[:,0], a[:,1], 80, 'g', 'o')
plt.scatter(b[:,0], b[:,1], 80, 'b', 's')
plt.scatter(test[:,0], test[:,1], 80, 'r', '*')

plt.show()
print(test)
print(p2)