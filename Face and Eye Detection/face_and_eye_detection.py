import numpy as np
import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
	ret, frame = cap.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.equalizeHist(gray)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 5)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = frame[y:y+h, x:x+w]
		eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=5, minSize=(20, 20))
		for (ex, ey, ew, eh) in eyes:
			eye_center = (x + ex + ew // 2, y + ey + eh // 2)
           	 	radius = int(0.3 * (ew + eh) / 2)
            		cv2.ellipse(roi_color, eye_center, (radius, radius), 0, 0, 360, (0, 0, 255), 5)


	cv2.imshow("frame", frame)
	if cv2.waitKey(1) == ord("q"):
        	break
cap.release()

	

	if cv2.waitKey(1) == ord("q"):
		break

cap.release()
cv2.destroyAllWindows()
