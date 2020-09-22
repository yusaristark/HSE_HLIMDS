BUTTON_PIN=5

import sys
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("push 3 times")
click_cnt = 0
while click_cnt < 3:
    inputValue = GPIO.input(BUTTON_PIN)
    if(inputValue == False):
        click_cnt = click_cnt + 1;
        print(click_cnt)
    sleep(1)
print("done")
GPIO.cleanup()