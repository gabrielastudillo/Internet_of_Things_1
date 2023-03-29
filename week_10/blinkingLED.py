#/usr/bin/python3
import RPi.GPIO as GPIO
import time
LED=18 # on this pin I will connect my LED
GPIO.setmode(GPIO.BCM) #I am using the BCM naming
GPIO.setup(LED, GPIO.OUT) #Pin 18 is an output
GPIO.setup(LED, GPIO.LOW) # Pin 18 starts in LOW state
blinks = 0 # initialize the blink
print ('Blinking starts')
while (blinks < 10): #let's do this 10 times
   GPIO.output(LED, GPIO.HIGH)
   time.sleep(1)
   GPIO.output(LED, GPIO.LOW)
   time.sleep(1)
   blinks=blinks + 1
   print('blinking...')
GPIO.cleanup() /close the door when you leave
print('done')
