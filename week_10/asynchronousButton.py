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

def backdoor(channel):
    GPIO.output(LED, GPIO.HIGH)   #LED ON
    print ("Back door")
    print('Edge detected on channel %s'%channel)
    time.sleep(0.1) #on just for a few
    GPIO.output(LED, GPIO.LOW) # LED OFF

def frontdoor(channel):
    GPIO.output(LED, GPIO.HIGH)   #LED ON
    print ("Front door")
    print('Edge detected on channel %s'%channel)
    time.sleep(0.1) #ON just for a few
    GPIO.output(LED, GPIO.LOW) # LED OFF    
    
GPIO.add_event_detect(BUTTON1, GPIO.FALLING, callback=backdoor)
GPIO.add_event_detect(BUTTON2, GPIO.FALLING, callback=frontdoor)     

try:
  while True:
      pass
except KeyboardInterrupt:
  GPIO.cleanup()

print("End of the program")
