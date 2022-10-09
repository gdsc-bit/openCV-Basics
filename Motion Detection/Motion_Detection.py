#Name:Ashish Ramesh
#Github ID : AshishRamesh

import cv2 as cv , pandas
from datetime import datetime

video = cv.VideoCapture(0)
first_frame = None
status_list = [None,None]
times = []
print("Press q to exit!!!")
while True :
    check,frame = video.read()
    cvt = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    cvt = cv.GaussianBlur(cvt,(21,21),0)
    status = 0

    if first_frame is None:
        first_frame = cvt
        continue
    
    delta_frame = cv.absdiff(first_frame,cvt)
    thres_frame = cv.threshold(delta_frame,50,255,cv.THRESH_BINARY)[1]
    thres_frame = cv.dilate(thres_frame,None,iterations=2)
    (cnts,_) = cv.findContours(thres_frame.copy(),cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv.contourArea(contour) <= 10000:
            continue
        status = 1
        (x,y,w,h) = cv.boundingRect(contour)
        cv.rectangle(frame,(x,y),(x+w , y+h),(0,0,255),3)

    status_list.append(status)
    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())

    cv.imshow('Video',frame)
    key = cv.waitKey(1)
    if key == ord('q'):
        if status == 1:
            times.append(datetime.now())
        break

video.release()
cv.destroyAllWindows()