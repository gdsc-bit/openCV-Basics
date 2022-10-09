# Importing the required library
import cv2

# We here make an object named as "video" that has the videocapture method
# 0 signifies that we are accessing the camera of the local system on which we are working.

video=cv2.VideoCapture(0)

# In this while loop we will run each frame for each loop.
while True:
  
  
    check,frame=video.read()
    
    
    cv2.imshow("FRAME",frame)
    
    
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
        
video.release()
cv2.destroyAllWindows
