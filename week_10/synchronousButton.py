#!/usr/bin/python3
import RPi.GPIO as GPIO

BUTTON1 = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON1, GPIO.IN, pull_up_down = GPIO.PUD_UP) #default UP
GPIO.wait_for_edge(BUTTON1, GPIO.FALLING)
print("Button was pressed")
GPIO.cleanup()
