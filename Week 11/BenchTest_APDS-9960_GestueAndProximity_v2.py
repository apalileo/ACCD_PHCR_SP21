"""
Gesture and proximity using 2 APDS9960 breakouts
with custom lib/adafruit_apds9960/apds9960.py file
"""

import board
import time
import digitalio
import busio
from adafruit_apds9960.apds9960 import APDS9960

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
    #print(proximity)
    apdsP.clear_interrupt()

    if killswitch.value:
        if gesture == UP:
            print("up")
        elif gesture == DOWN:
            print("down")
        elif gesture == LEFT:
            print("left")
        elif gesture == RIGHT:
            print("right")
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