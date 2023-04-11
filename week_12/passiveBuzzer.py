#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

PBUZZER = 17

GPIO.setmode(GPIO.BCM)       # Numbers pins by GPIO number
GPIO.setup(PBUZZER, GPIO.OUT)   # Set pin mode as output
GPIO.output(PBUZZER, GPIO.LOW)  # Starts OFF

p = GPIO.PWM(PBUZZER, 50) # init frequency: 50HZ
p.start(50)  # Duty cycle: 50%

try:
	while True:
		for f in range(100, 2000, 100):
			p.ChangeFrequency(f)
			time.sleep(0.2)
		for f in range(2000, 100, -100):
			p.ChangeFrequency(f)
			time.sleep(0.2)
except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()
