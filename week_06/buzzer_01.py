from gpiozero import Buzzer
import time
pin = 17
bz = 0
def setup():
# Instructions to set up your hardware  # Ex: initialize your objects
# Give objects a default value
   global bz
   bz = Buzzer(pin)

def loop():
# infinite loop used for testing 
   global bz
   while True:
      bz.on()
      time.sleep(1)
      bz.off()
      time.sleep(1)
def destroy():
   global bz
   print("program ended by user")
   bz.off()

if __name__ == '__main__':# Program starts from here
   print("Press Ctrl+C to end the program...")
   setup()
   try:
      loop()
   except KeyboardInterrupt: # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
      destroy()
