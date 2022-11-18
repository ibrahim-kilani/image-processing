import cv2
import numpy as np
from matplotlib import pyplot as plt

Input = cv2.imread('Sum.png',0)

horizontalSobelFilter = np.array([[-1, -2, -1], [0, 0, 0], [1,2,1]], float)

horizontalOutput = cv2.filter2D(Input,-1,horizontalSobelFilter)

virticalSobelFilter = np.array([[-1, 0, 1], [-2, 0, 2], [-1,0,1]], float)

virticalOutput = cv2.filter2D(Input,-1,virticalSobelFilter)

Output= cv2.add(horizontalOutput,virticalOutput)

# cv2.imwrite('SobelFilter.png',Output)

plt.imshow(Output, cmap = 'gray', interpolation='bicubic')
plt.show()