LED_PIN=23

import sys
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
for i in range(10):
	GPIO.output(LED_PIN, True)
	sleep(1.5)
	GPIO.output(LED_PIN, False)
	sleep(1.5)
GPIO.cleanup()

