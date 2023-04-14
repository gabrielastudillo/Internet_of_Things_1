#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

LED=18
BUTTON1 = 24
BUTTON2 = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(BUTTON1, GPIO.IN, pull_up_down = GPIO.PUD_UP) #default UP
GPIO.setup(BUTTON2, GPIO.IN, pull_up_down = GPIO.PUD_UP) #default UP

try:
  while True:
    if (GPIO.input(BUTTON1) == GPIO.LOW):
       print ("Back door")
       GPIO.output(LED, GPIO.HIGH)   #LED ON
    elif (GPIO.input(BUTTON2) == GPIO.LOW):
       print ("Front door")
       GPIO.output(LED, GPIO.HIGH) #LED ON
    else:
       GPIO.output(LED, GPIO.LOW) #otherwise LED OFF
    time.sleep(0.1)
except KeyboardInterrupt:
  GPIO.cleanup()
print("End of the test")
#test1
