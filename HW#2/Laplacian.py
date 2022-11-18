import cv2
import numpy as np
from matplotlib import pyplot as plt

Input = cv2.imread('Sum.png',0)

LaplacianFilter = np.array([[0, 1, 0], [1, -4, 1], [0,1,0]], float)

Output = cv2.filter2D(Input,-1,LaplacianFilter)

# cv2.imwrite('LaplacianFilter.png',Output)

plt.imshow(Output, cmap = 'gray', interpolation='bicubic')
plt.show()

