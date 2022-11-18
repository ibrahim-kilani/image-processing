import cv2
import numpy as np
from matplotlib import pyplot as plt

orginal = cv2.imread('Sum.png',0)

AveragingFilter = cv2.blur(orginal,(3,3),borderType=cv2.BORDER_REPLICATE)

# cv2.imwrite('AveragingFilter.png',AveragingFilter)

plt.imshow(AveragingFilter, cmap = 'gray', interpolation='bicubic')
plt.show()

