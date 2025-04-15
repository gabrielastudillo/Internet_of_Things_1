from tkinter import *
from gpiozero import LED

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()

        # Initialize LEDs using gpiozero
        self.red_led = LED(21)
        self.yellow_led = LED(20)

        # Internal state tracking
        self.red_led_state = False
        self.yellow_led_state = False

        self.create_widgets()

    def create_widgets(self):
        self.REDbutton = Button(self, text="Red LED", bg="red", command=self.toggle_red_led)
        self.REDbutton.grid(row=0, column=0, padx=10, pady=10)

        self.YELLOWbutton = Button(self, text="Yellow LED", bg="yellow", command=self.toggle_yellow_led)
        self.YELLOWbutton.grid(row=0, column=1, padx=10, pady=10)

    def toggle_red_led(self):
        if self.red_led_state:
            self.red_led.off()
        else:
            self.red_led.on()
        self.red_led_state = not self.red_led_state

    def toggle_yellow_led(self):
        if self.yellow_led_state:
            self.yellow_led.off()
        else:
            self.yellow_led.on()
        self.yellow_led_state = not self.yellow_led_state

# GUI setup
root = Tk()
root.title("LED Control")
root.geometry("400x200")
app = Application(root)
root.mainloop()
