"""
Chapter 4: Shapes & Text
"""
import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
cv2.imshow("Image", img)

# The ':' means the limits of where the Image is coloured
img[:] = 255, 0, 0
cv2.imshow("Image Blue", img)

# Just to make the background black for the other examples
img[:] = 0, 0, 0

# cv2.line(Which image it appears on, (starting coordinates), (ending coordinates), (colour in BGR), thickness)
cv2.line(img, (0, 0), (300, 300), (0, 0, 255), 3)
cv2.imshow("Image with Red Line halfway", img)

cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 255), 3)
cv2.imshow("Image with Yellow Line full", img)

# Same parameters as the line
cv2.rectangle(img, (0, 0), (100, 200), (0, 255, 0), 2)
cv2.imshow("Image with hollow rectangle", img)

# Change the thickness parameter into 'cv2.FILLED' to make it filled instead of hollow
cv2.rectangle(img, (0, 0), (100, 200), (0, 255, 0), cv2.FILLED)
cv2.imshow("Image with filled rectangle", img)

# cv2.circle(Which image it appears on, (starting coordinates), radius, (colour in BGR), thickness)
cv2.circle(img, (400, 50), 30, (255, 255, 0), 5)
cv2.imshow("Image with hollow blue circle", img)

cv2.circle(img, (400, 50), 30, (255, 255, 0), cv2.FILLED)
cv2.imshow("Image with filled blue circle", img)

# cv2.putText(Which image it appears on, "Text", (starting coordinates), font, scale, (colour in BGR), thickness)
# Scale changes the font size, thickness changes the 'boldness', it can be a decimal too.
cv2.putText(img, "OpenCV", (200, 100), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 150, 0), 3)
cv2.imshow("Image with green text", img)

cv2.waitKey(0)

"""
Press 'Q' to quit examples when running
"""
