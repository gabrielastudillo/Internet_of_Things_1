import RPi.GPIO as GPIO
LED = 18
FREQUENCY = 1
DUTY = 50
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
blink = GPIO.PWM(LED,FREQUENCY)
try:
  blink.start(DUTY)
  while True:
    pass
except KeyboardInterrupt:
  blink.stop()
finally:
  GPIO.cleanup()
