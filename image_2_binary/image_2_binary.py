import cv2
input_image = cv2.imread()     #path to your image
width, height, channels = input_image.shape
for i in range(width):
  for j in range(height):
    r,g,b = input_image[i,j]
    lumino = ((0.299*r + 0.587*g + 0.114*b)/255)
    if(lumino < 0.5):
      a = 0
    else:
      a = 1
    print(a, end = "")
