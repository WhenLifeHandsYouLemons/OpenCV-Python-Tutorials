"""
Chapter 3: Resizing and cropping
"""
import cv2
import numpy as np

img = cv2.imread("Resources/lena.jpg")
print(img.shape)
cv2.imshow("Image", img)

imgResize = cv2.resize(img, (300, 200))
cv2.imshow("Image Resize", imgResize)

imgCropped = img[0:200, 200:500]
cv2.imshow("Image Cropped", imgCropped)

cv2.waitKey(0)
