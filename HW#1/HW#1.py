
import cv2
import numpy as np
from matplotlib import pyplot as plt

Sum=cv2.imread('ImagesForHW/Fig1.tif',0)
Sum = np.float16(Sum)
for index in range(2,101):
    img = cv2.imread('ImagesForHW/Fig' + str(index) + '.tif', 0)
    Sum += img

Sum /= 100

plt.imshow(Sum, cmap = 'gray', interpolation='bicubic')
plt.show()

