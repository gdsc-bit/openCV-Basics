#Import the required libraries
import cv2

#Object to create an initial video frame reference
video=cv2.VideoCapture(0)

#Setting the params such as height,width of the window
video.set(3,640)
video.set(4,480)
video.set(10,400)

#Proccesing of each frame under this while loop
while True:
    check,frame=video.read()
    edges = cv2.Canny(frame,100,150)#We can put values between 0 to 255 according to the thresholding effect user wants
    cv2.imshow("EDGE",edges)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
video.release()
cv2.destroyAllWindows
