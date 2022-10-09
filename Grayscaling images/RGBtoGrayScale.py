#Grayscaling is the process of converting an image from other color spaces e.g. RGB, CMYK, HSV, etc. to shades of gray.
#Importance of grayscaling 
#Dimension reduction: For example, In RGB images there are three color channels and three dimensions while grayscale images are single-dimensional.
#Reduces model complexity: Consider training neural articles on RGB images of 10x10x3 pixels. The input layer will have 300 input nodes. On the other hand, the same neural network will need only 100 input nodes for grayscale images.
#For other algorithms to work: Many algorithms are customized to work only on grayscale images e.g. Canny edge detection function pre-implemented in the OpenCV library works on Grayscale images only.

<h2>Let’s learn the different image processing methods to convert a colored image into a grayscale image.</h2>
<h2>Method 1: Using the cv2.cvtColor() function</h2>
import cv2
image = cv2.imread('C:\\Documents\\full_path\\tomatoes.jpg')
cv2.imshow('Original', image)
cv2.waitKey(0)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale', gray_image)
cv2.waitKey(0) 
cv2.destroyAllWindows()
