import cv2
import numpy as np
from matplotlib import pyplot as plt

imm = cv2.imread('(7) Median3x3Itt3OnMedian.bmp', 0)
im1, contours, hierarchy = cv2.findContours(imm, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contoursLength = len(contours)
arrayOfPolygons = []
i=0
for i in range(0,contoursLength):
    cnt = contours[i]
    epsilon = 0.045*cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsilon,True)

    arrayOfPolygons.append(approx)

    imm = cv2.imread('(7) Median3x3Itt3OnMedian.bmp', 1)

    cv2.drawContours(imm, [approx], 0, (0, 0, 255), 1)

    cv2.imwrite('ApproxContor[' + str(i) + '].bmp', imm)
    i=i+1



