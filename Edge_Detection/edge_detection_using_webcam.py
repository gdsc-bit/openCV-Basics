# edge detection is useful for a sharp change in the intensity or the color of the image
#basically detecting te line which seperates two different colors
#three types of methods r available
# 1 : sobel: not a good method used for horizontal and vertical detection(classical method)
# 2:  laplacian: another method for edge detection
# 3: most commonly used method CANNY


import cv2
import numpy as np

cap=cv2.VideoCapture(0)


while True:
          _,frame=cap.read()
          gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

          sobelx=cv2.Sobel(gray,cv2.CV_64F,1,0)
          sobely=cv2.Sobel(gray,cv2.CV_64F,0,1)
          # for horizontal detection we kept x axis onn by writing 1 and y axis as off vice versa for y axis

          laplacian=cv2.Laplacian(gray,cv2.CV_64F)

          canny=cv2.Canny(gray,100,150)
          #so here the image pixels lying between 0 to 100 would not be detected
          #between 150 and 255 it would be detected
          # and betwen 100 and 150 it depends on the method

          cv2.imshow('gray image',gray)
          cv2.imshow('sobel-x',sobelx)
          cv2.imshow('sobel-y',sobely)
          cv2.imshow('laplacian',laplacian)
          cv2.imshow('canny',canny)
          key=cv2.waitKey(1)
          if key==ord('q'):
                    break
                    
cap.release()
cv2.destroyAllWindows()
