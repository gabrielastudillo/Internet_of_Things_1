#!/usr/bin/env python3
from gpiozero import LED, Button
from time import sleep
# ============================
# Pin Assignments
# ============================
RED_LED = 17        # Red LED connected to pin 17
BLUE_LED = 27       # Blue LED connected to pin 27
RED_BUTTON = 5      # Red button connected to pin 5
BLUE_BUTTON = 6     # Blue button connected to pin 6


def setup():
    global red_led, blue_led, red_btn, blue_btn

    # Initialize LED objects
    red_led = LED(RED_LED)
    blue_led = LED(BLUE_LED)

    # Initialize Button objects
    red_btn = Button(RED_BUTTON, pull_up=True, bounce_time=0.05)
    blue_btn = Button(BLUE_BUTTON, pull_up=True, bounce_time=0.05)

    # Make sure LEDs start OFF
    red_led.off()
    blue_led.off()

    print("[SETUP] Hardware initialized.")


def loop():
    while True:
        # Red button controls red LED
        if red_btn.is_pressed:
            red_led.on()
        else:
            red_led.off()

        # Blue button controls blue LED
        if blue_btn.is_pressed:
            blue_led.on()
        else:
            blue_led.off()

        sleep(0.05)   # small delay to avoid CPU overuse


def destroy():
    # Turn LEDs off
    red_led.off()
    blue_led.off()
    red_led.close()
    blue_led.close() 
    print("Program terminated. Resources released. Bye!")


# ============================
# Program entry point
# ============================
if __name__ == '__main__':
    print("Press Ctrl+C to end the program...")
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
