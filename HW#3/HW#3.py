
import cv2

def determineColor(Hue,Saturation):

    color = "None"
    if Saturation==0:
        color = "White"
    elif Hue >=235 or Hue < 20 :
        color = "Red"
    elif Hue >= 20 and Hue < 60:
        color = "Yellow"
    elif Hue >= 60 and Hue < 100:
        color = "Green"
    elif Hue >= 100 and Hue < 140:
        color = "Cyan"
    elif Hue >= 140 and Hue < 180:
        color = "Blue"
    elif Hue >= 180 and Hue < 220:
        color = "Magenta"

    return color

def determineShape(shapesCount,polygonLength,shapesColors,Hue,Saturation):
    indexOfShapesColorsList = None
    if polygonLength==3:
        shapesCount[0]=shapesCount[0]+1
        indexOfShapesColorsList = 0
    elif polygonLength==4:
        shapesCount[1]=shapesCount[1]+1
        indexOfShapesColorsList = 1
    else:
        shapesCount[2]=shapesCount[2]+1
        indexOfShapesColorsList = 2

    shapesColors[indexOfShapesColorsList].append(determineColor(Hue, Saturation))

imm = cv2.imread('(7) Median3x3Itt3OnMedian.bmp', 0)
im1, contours, hierarchy = cv2.findContours(imm, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contoursLength = len(contours)
print("The number of real shapes in the image = " + str(contoursLength))

arrayOfPolygons = []

for i in range(0,contoursLength):
    cnt = contours[i]
    epsilon = 0.045*cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsilon,True)

    arrayOfPolygons.append(approx)

imgBGR = cv2.imread('(3) Median5x5Itt7OnGaussianBlur.bmp', 1)
imgHSV = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2HSV_FULL)

shapesCount=[0,0,0]
shapesColors=[[],[],[]]

for polygon in arrayOfPolygons:
    x = 0
    y = 0
    for point in polygon:
        x+=point[0,0]
        y+=point[0,1]
    polygonLength = len(polygon)

    x/=polygonLength
    y/=polygonLength

    Hue = imgHSV[y,x,0]
    Saturation=imgHSV[y,x,1]

    determineShape(shapesCount, polygonLength,shapesColors,Hue,Saturation)

print("#Triangle = " + str(shapesCount[0]) + " / " "#Rectangle = " + str(shapesCount[1]) + " / " "#Circle = " + str(shapesCount[2]))

shapes = ['Triangles','Rectangles','Circles']
i=0

for shapeColors in shapesColors:

    print("----------------------------")
    print("Colors of " + shapes[i] + " :")

    for color in shapeColors:
        print(color)

    i=i+1