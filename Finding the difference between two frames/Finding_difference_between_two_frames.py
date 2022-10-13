#Name:Ashish Ramesh
#Github ID : AshishRamesh

import cv2 as cv 

video = cv.VideoCapture(0)
first_frame = None

print("Press q to exit!!!")
while True :
    check,frame = video.read()
    cvt = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)#Converting video input to gray scale
    cvt = cv.GaussianBlur(cvt,(21,21),0)

    if first_frame is None:
        first_frame = cvt #Saves the first frame to cvt
        continue

    #The difference between the first frame(cvt) and current frame is being checked
    delta_frame = cv.absdiff(first_frame,cvt) 
    thres_frame = cv.threshold(delta_frame,50,255,cv.THRESH_BINARY)[1]#threshold is created from the delta frame 
    thres_frame = cv.dilate(thres_frame,None,iterations=2)#threshhold  frame is diluted for better visibility
    (cnts,_) = cv.findContours(thres_frame.copy(),cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)# The points where diffrence is found is saved

    #To exit the program
    cv.imshow('Video',frame)#The input that is seen by the camera
    cv.imshow('Delta Frame',delta_frame)#This Frame shows the difference between the first frame and the successeding frames 
    cv.imshow('Threshold Frame',thres_frame)#Coverts the difference to binary(Black and white)for optimized results
    key = cv.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv.destroyAllWindows()