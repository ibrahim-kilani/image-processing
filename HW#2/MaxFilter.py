import cv2
import numpy as np
from matplotlib import pyplot as plt

Input = cv2.imread('Sum.png',0)

kernel = np.ones((3,3),np.uint8)
Output = cv2.dilate(Input,kernel,iterations = 1)

# cv2.imwrite('MaxFilter.png',Output)

plt.imshow(Output, cmap = 'gray', interpolation='bicubic')
plt.show()

