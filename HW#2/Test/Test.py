import cv2
import numpy as np
from matplotlib import pyplot as plt

Input = cv2.imread('orginal.png',0)

kernel = np.ones((3,3),np.uint8)
dilation = cv2.dilate(Input,kernel,iterations = 1)

# cv2.imwrite('MaxFilter.png',dilation)

plt.imshow(dilation, cmap = 'gray', interpolation='bicubic')
plt.show()

