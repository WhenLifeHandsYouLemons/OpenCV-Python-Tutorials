"""
Chapter 9: Face Detection
"""
import cv2
import numpy as np

# Start camera
cap = cv2.VideoCapture(0)
"""The '3' specifies the width of the video/image"""
cap.set(3, 640)
"""The '4' specifies the height of the video/image"""
cap.set(4, 480)
"""The '10' specifies the brightness of the video/image"""
cap.set(10, 100)

"""1st one is orange,
   2nd one is green,
   3rd one is yellow,
   4th one is light blue.
   This list is the colours that will be detected.
   Use the 'Colour Finder.py' file to find out the values.
   The format for a colour is '[h_min, s_min, v_min, h_max, s_max, v_max]'.
   You can add more colours to the bottom of the list."""
myColours = [[4, 245, 98, 30, 255, 255],
             [60, 134, 46, 92, 186, 255],
             [17, 229, 89, 27, 255, 123],
             [92, 195, 81, 111, 255, 121],]

"""Colour values in BGR.
   This list is the colours that are drawn on the screen.
   You can add more colours to the bottom."""
myColourValues = [[51, 153, 255],
                  [0, 100, 0],
                  [0, 255, 255],
                  [255, 75, 75]]

""""Written in this format myPoints = [x, y, colourID]"""
myPoints = []


def findColour(img, myColours, myColourValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for colour in myColours:
        lower = np.array(colour[0:3])
        upper = np.array(colour[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x ,y = getContours(mask)
        cv2.circle(imgResult, (x, y), 10, myColourValues[count], cv2.FILLED)
        if x != 0 and y != 0:
            newPoints.append([x, y, count])
        count = count + 1
#        cv2.imshow(str(colour[0]), mask)
    return newPoints

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    x, y, w, h = 0, 0, 0, 0

    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area >= 100:
            # cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)

            peri = cv2.arcLength(cnt, True)

            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)

            x, y, w, h = cv2.boundingRect(approx)
    return x + w // 2, y

def drawOnCanvas(myPoints, myColourValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColourValues[point[2]], cv2.FILLED)

while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColour(img, myColours, myColourValues)

    if len(newPoints) != 0:
        for newPoint in newPoints:
            myPoints.append(newPoint)
    if len(myPoints) != 0:
        drawOnCanvas(myPoints, myColourValues)

    # cv2.imshow("Plain Video", img)
    cv2.imshow("Video with detection", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

"""
Press 'Q' to quit examples
"""