"""
Chapter 2: Basic functions
"""
import cv2
import numpy as np
print("OpenCV Package Imported")
print("Numpy Package Imported")

img = cv2.imread("Resources/lena.jpg")

imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grey Image", imgGrey)

imgBlur = cv2.GaussianBlur(imgGrey, (7, 7), 0)
cv2.imshow("Blur Image", imgBlur)

# This is used for edge-detection in an image (or a video)
# The '100' values are the threshold of the edge-detection
imgCanny = cv2.Canny(img, 100, 100)
cv2.imshow("Canny Image", imgCanny)

kernel = np.ones((5, 5), np.uint8)
# The value '5' is to change the thickness of the dilation
imgDilation = cv2.dilate(imgCanny, kernel, iterations=5)
cv2.imshow("Dilation Image of the canny image", imgDilation)

imgEroded = cv2.erode(imgDilation, kernel, iterations=3)
cv2.imshow("Eroded Image of the dilation image", imgEroded)

cv2.waitKey(0)

"""
Press 'Q' to exit the example or cross out all the tabs.
"""
