import cv2
import numpy as np
from matplotlib import pyplot as plt

orginal = cv2.imread('Sum.png',0)

MedianFilter = cv2.medianBlur(orginal,3)

# cv2.imwrite('MedianFilter.png',MedianFilter)

plt.imshow(MedianFilter, cmap = 'gray', interpolation='bicubic')
plt.show()

