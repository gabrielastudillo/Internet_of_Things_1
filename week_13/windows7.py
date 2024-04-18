from tkinter import *
import RPi.GPIO as GPIO
from time import sleep

class Application(Frame):
  REDLED=21
  YELLOWLED=20
  REDLED_state=True
  YELLOWLED_state=True
  
    def __init__(self,master):
        super(Application, self).__init__(master)
        self.grid()
        self.init_hardware()
        self.create_widgets()

    def init_hardware(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.REDLED, GPIO.OUT)
        GPIO.setup(self.REDLED, GPIO.LOW)
        GPIO.setup(self.YELLOWLED, GPIO.OUT)
        GPIO.setup(self.YELLOWLED, GPIO.LOW)
        
    def create_widgets(self):
        self.REDbutton = Button (self, text="Red Led", bg="red", command=self.RedButton)

root = Tk()
root.title("This is a test window")
root.geometry("800x400")
app = Application(root)
app.mainloop()
