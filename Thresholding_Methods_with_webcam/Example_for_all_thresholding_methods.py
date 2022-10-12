# Import the required library
import cv2

# Create an object of the videocapture
video=cv2.VideoCapture(0)

# Processing each frame here
while True:
    check,frame=video.read()
    
    # Converting the frame into GRAY from it's BGR format
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    # Different Thresholding methods available in opencv
    # Refer documentation for accurate explanation of each of them
    
    # The params may be changed accoding to the convinience
    _,thresh=cv2.threshold(frame,100,200,cv2.THRESH_BINARY)
    _,thresh_inv=cv2.threshold(frame,127,255,cv2.THRESH_BINARY_INV)
    _,thresh_tru=cv2.threshold(frame,127,255,cv2.THRESH_TRUNC)
    _,thresh_to0=cv2.threshold(frame,127,255,cv2.THRESH_TOZERO)
    _,thresh_to0i=cv2.threshold(frame,127,255,cv2.THRESH_TOZERO_INV)
    
    
    # Showing each and every Frame(including the threshold frame)
    cv2.imshow("Original",frame)
    cv2.imshow("Threshold",thresh)
    cv2.imshow("Thresh_inverse",thresh_inv)
    cv2.imshow("Thresh_Truncate",thresh_tru)
    cv2.imshow("Thresh_ToZero",thresh_to0)
    cv2.imshow("Thresh_to_Inverse",thresh_to0i)
    
    
    
    #Pres q to exit
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
video.release()
cv2.destroyAllWindows
