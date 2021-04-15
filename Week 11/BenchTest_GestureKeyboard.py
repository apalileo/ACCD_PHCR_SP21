"""
Gesture and proximity using 2 APDS9960 breakouts on
Adafruit Playground Bluefruit board with busio
and custom lib/adafruit_apds9960/apds9960.py file
sending WASD and ENTER commands to Adobe Xd prototype
"""

import board
import time
import digitalio
import busio
import usb_hid
from adafruit_apds9960.apds9960 import APDS9960
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

killswitch = digitalio.DigitalInOut(board.SLIDE_SWITCH)
killswitch.direction = digitalio.Direction.INPUT
killswitch.pull = digitalio.Pull.UP

i2cA = busio.I2C(board.A1, board.A2)
apdsG = APDS9960(i2cA)
apdsG.enable_gesture = True
apdsG.enable_proximity = True

# default gesture_proximity_threshold = 50 (range 0-255)"""
apdsG.gesture_proximity_threshold = 0
# default gesture_gain = 2 (range 0-3)"""
apdsG.gesture_gain = 3
# default gesture_fifo_threshold = 1 (range 0-3)"""
apdsG.gesture_fifo_threshold = 3
# default gesture_dimensions = 1 (range 0-3)"""
apdsG.gesture_dimensions = 3
# default rotation = 0 (possible, 0, 90, 180, 270)
apdsG.rotation = 90

i2cB = busio.I2C(board.A3, board.A4)
apdsP = APDS9960(i2cB)
apdsP.enable_proximity = True

# keyboard
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

# basic gesture directions
NONE = 0
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# "press" gesture variables
press = False
pressPrev = press
pressThresh = 4

while True:
    gesture = apdsG.gesture()
    proximity = apdsP.proximity
    apdsP.clear_interrupt()

    if killswitch.value:
        if gesture == UP:
            print("up")
            kbd.press(Keycode.W)
            kbd.release_all()
        elif gesture == DOWN:
            print("down")
            kbd.press(Keycode.S)
            kbd.release_all()
        elif gesture == LEFT:
            print("left")
            kbd.press(Keycode.A)
            kbd.release_all()
        elif gesture == RIGHT:
            print("right")
            kbd.press(Keycode.D)
            kbd.release_all()
        elif gesture == NONE:
            if proximity >= pressThresh:
                press = True
                # allow time to prevent "double press"
                time.sleep(0.300)
            else:
                press = False

        if press != pressPrev:
            pressPrev = press
            if press:
                print("press")
                kbd.press(Keycode.RETURN)
                kbd.release_all()
