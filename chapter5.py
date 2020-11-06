"""
Chapter 5: Warp Perspective
"""
import cv2
import numpy as np

width, height = 250, 350

img = cv2.imread("Resources/cards.jpg")

# Normal image
cv2.imshow("Image", img)

# Warped image
pts1 = np.float32([[207, 115], [334, 144], [90, 269], [229, 310]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))
cv2.imshow("Image with Warp", imgOutput)

cv2.waitKey(0)
"""
Exit the examples by pressing 'Q'
"""
