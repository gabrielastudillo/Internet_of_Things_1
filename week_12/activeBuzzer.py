#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

BUZZER = 17    # GPIO17 / pin11

def setup():
	GPIO.setmode(GPIO.BCM)        # Numbers pins by physical location
	GPIO.setup(BUZZER, GPIO.OUT)   # Set pin mode as output
	GPIO.output(BUZZER, GPIO.HIGH) # Set pin to high(+3.3V) to off the beep

def loop():
	while True:
		GPIO.output(BUZZER, GPIO.LOW)
		time.sleep(0.1)
		GPIO.output(BUZZER, GPIO.HIGH)
		time.sleep(0.1)

def destroy():
	GPIO.output(BUZZER, GPIO.HIGH)    # beep off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	print 'Press Ctrl+C to end the program...'
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()
