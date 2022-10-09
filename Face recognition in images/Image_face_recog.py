#Name:Ashish Ramesh
#Github ID : AshishRamesh

import cv2 as cv

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

file1 = input('Enter Location of image : ')

img = cv.imread()
grey_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
face = face_cascade.detectMultiScale(grey_img,
scaleFactor = 2,
minNeighbors = 5)

for x,y,w,h in face:
    img = cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

resized = cv.resize(img, (int(img.shape[1]/3),int(img.shape[0]/3)))
cv.imshow('Image',resized)
cv.waitKey(0)
cv.destroyAllWindows()