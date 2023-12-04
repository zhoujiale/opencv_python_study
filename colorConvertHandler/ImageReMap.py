import cv2
import numpy as np
img = cv2.imread("../lena.jpg")
rows, cols = img.shape[:2]
mapx = np.zeros(img.shape[:2], np.float32)
mapy = np.zeros(img.shape[:2], np.float32)
for i in range(rows):
    for j in range(cols):
        if 0.2*cols < i < 0.8*cols and 0.2*rows < j < 0.8*rows:
            mapx.itemset((i, j), 5/3 * j - cols * 0.6 + 0.6)
            mapy.itemset((i, j), 5/3 * i - cols * 0.6 + 0.6)
        else:
            mapx.itemset((i, j), 0)
            mapy.itemset((i, j), 0)
rst = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)
cv2.imshow("original", img)
cv2.imshow("result", rst)
cv2.waitKey()
cv2.destroyAllWindows()
