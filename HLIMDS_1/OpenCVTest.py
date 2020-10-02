import cv2
import numpy as np

cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

cam = cv2.VideoCapture(0)

while True:
	ret, img = cam.read()
	print(ret)
	height, width = img.shape[:2]
	print(width, 'x', height)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = faceCascade.detectMultiScale(gray, scaleFactor= 1.3, minNeighbors= 4, minSize=(30, 30))
	faces_detected = "Лиц обнаружено: " + format(len(faces))
	print(faces_detected)
	for (x, y, w, h) in faces:
		cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)
		print(x, ' ', y, ' ', w, ' ', h)
	cv2.imshow('my_cam', img)
	if cv2.waitKey(10) == 27:
		break

cam.release()
cv2.destroyAllWindows()
