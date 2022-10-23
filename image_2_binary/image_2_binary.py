from PIL import Image 
input_image = Image.open()     #path to your image
pixel_map = input_image.load()
width, height = input_image.size
for i in range(width):
  for j in range(height):
    r,g,b = input_image.get.pixel((i,j))
    lumino = ((0.299*r + 0.587*g + 0.114*b)/255)
    if(lumino < 0.5):
      a = 0
    else:
      a = 1
    print(a, end = "")
