"""
Chapter 1: Read images, videos and live webcam video
"""
import cv2
print("OpenCV Package Imported")

"""
Used for reading and displaying images
"""
img = cv2.imread("Resources/lena.jpg")
cv2.imshow("Output", img)
cv2.waitKey(0)

"""
Used for reading and displaying videos
"""
cap = cv2.VideoCapture("Resources/test_video.mp4")

#while True:
#    success, img = cap.read()
#    cv2.imshow("Video", img)
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break

"""
Used for getting video from the webcam (change the first 0 to any other number for other cameras that are connected) and
 displaying it
"""
cap = cv2.VideoCapture(0)
"""The '3' specifies the width of the video/image"""
cap.set(3, 640)
"""The '4' specifies the height of the video/image"""
cap.set(4, 480)
"""The '10' specifies the brightness of the video/image"""
cap.set(10, 100)

#while True:
#    success, img = cap.read()
#    cv2.imshow("Video", img)
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break

"""
Press 'Q' to quit the window when the video example is playing.
"""
