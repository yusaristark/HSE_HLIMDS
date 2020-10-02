import cv2
import numpy
import sys
import RPi.GPIO as GPIO
from time import sleep

LED_PIN=23
BUTTON_PIN=5
SERVO_PIN=25

cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

cam = cv2.VideoCapture(0)

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SERVO_PIN, GPIO.OUT)

pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start(0)

def setAngle(angle):
	duty=angle/18+2
	GPIO.output(SERVO_PIN, True)
	pwm.ChangeDutyCycle(duty)
	GPIO.output(SERVO_PIN, False)
	pwm.ChangeDutyCycle(0)

pos = 90
setAngle(pos)
sleep(1)

while True:
	ret, img = cam.read()
	height, width = img.shape[:2]
	moveCam = False
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = faceCascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30))
	if len(faces)!=0:
		GPIO.output(LED_PIN, True)
		moveCam = True
	else:
		GPIO.output(LED_PIN, False)
	inputValue = GPIO.input(BUTTON_PIN)
	if inputValue == True:
		for (x, y, w, h) in faces:
			cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)
	if moveCam == True:
		for (x, y, w, h) in faces:
			if x+(w/2) > width/2:
				pos = pos + 1
				setAngle(pos)
			elif x+(w/2) < width/2:
				pos = pos - 1
				setAngle(pos)

	cv2.imshow('my_cam', img)

	if cv2.waitKey(10) == 27:
		break

cam.release()
cv2.destroyAllWindows()
GPIO.cleanup()
