import numpy as np
import cv2

capture = cv2.VideoCapture(0)

while True:
	ret, frame = capture.read()
	width = int(capture.get(3))
	height = int(capture.get(4))

	# drawing lines, rectangles
	image = cv2.line(frame, (0, 0), (width, height), (255, 0, 255), 10)
	image = cv2.line(image, (width, 0), (0, height), (255, 255, 0), 10)
	image = cv2.rectangle(image, (100, 100), (200, 200), (0, 255, 0), 5)
	image = cv2.circle(image, (400, 400), 50, (0, 0, 255), -1)
	font = cv2.FONT_HERSHEY_SIMPLEX
	image = cv2.putText(image, "OpenCV is good!", (10, height-10), font, 1, (255, 255, 255), 4, cv2.LINE_AA)

	cv2.imshow("frame", image)

	if cv2.waitKey(1) == ord("q"):
		break

capture.release()
cv2.destroyAllWindows()
