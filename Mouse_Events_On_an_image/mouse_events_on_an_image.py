# Mouse Events r of great help they enable us to draw using the mouse

# For example:: during object tracking we make rectangle around the image using specified code
#and we need to get the points and then plot it
# it would be much easier if we directly draw the rectangle using mouse events around the object

import cv2
import numpy as np


drawing=False
point1=()
point2=()


def mouse_drawing(event,x,y,laggs,params):
          if event==cv2.EVENT_LBUTTONDOWN:
                    circle.append((x,y))

          
          global point1,point2,drawing
          if event==cv2.EVENT_RBUTTONDOWN:
                    if drawing is False:
                              drawing=True
                              point1=(x,y)
                              print(point1)
                    else:
                              drawing=False
          elif event==cv2.EVENT_MOUSEMOVE:
                    if drawing is True:
                              point2=(x,y)
                              print(point2)

frame=cv2.imread("b-tiger.jpg") #enter the image in single or double quotes e.g:"image.jpg"
circle=[]
cv2.namedWindow('Frame')
cv2.setMouseCallback('Frame',mouse_drawing)#the first argument is in which frame we need to use events
#second is the function we will be calling todo a mouse activity

for centre in circle:
    cv2.circle(frame,centre,5,(255,0,255),-1)

if point1 and point2:
        cv2.rectangle(frame,point1,point2,(0,255,0),3)

                              
cv2.imshow('Frame',frame)

cv2.waitKey(0)
cv2.destroyAllWindows()
