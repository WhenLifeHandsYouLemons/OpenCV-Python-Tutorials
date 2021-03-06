"""
Chapter 9: Face Detection
"""
import cv2

faceCascade = cv2.CascadeClassifier("Resources/Haarcascades/haarcascade_frontalface_default.xml")

img = cv2.imread("Resources/face.jpg")
img = cv2.resize(img, (512, 512))
cv2.imshow("Result", img)

imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGrey, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)

cv2.imshow("Result", img)

cv2.waitKey(0)
"""
Press 'Q' to exit examples
"""
