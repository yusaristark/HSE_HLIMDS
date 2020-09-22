SERVO_PIN=25

import sys
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start(0)

def SetAngle(angle):
	duty = angle/18+2
	GPIO.output(SERVO_PIN, False)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(SERVO_PIN, False)
	pwm.ChangeDutyCycle(0)
print("angle 0")
SetAngle(0)
print("angle 45")
sleep(0.5)
SetAngle(45)
print("angle 90")
sleep(0.5)
SetAngle(90)
print("angle 180")
sleep(0.5)
SetAngle(180)
sleep(0.5)
print("done")
GPIO.cleanup()
