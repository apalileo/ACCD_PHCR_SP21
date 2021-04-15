"""
APDS9960 gestures to rotate mouse wheel

Killswitch from Arnie Martin's
CircuitPlayground_Mouse_Buttons.py
https://gist.github.com/RealAbsurdity/ed00a16b342994796a49fb57aaa8ae6b

Adafruit HID Library referenced for mouse
https://circuitpython.readthedocs.io/projects/hid/en/latest/
"""

import board
import time
import digitalio
import busio
import usb_hid
from adafruit_hid.mouse import Mouse
from adafruit_apds9960.apds9960 import APDS9960

killswitch = digitalio.DigitalInOut(board.SLIDE_SWITCH)
killswitch.direction = digitalio.Direction.INPUT
killswitch.pull = digitalio.Pull.UP

mouse = Mouse(usb_hid.devices)

i2c = busio.I2C(board.SCL, board.SDA)
apds = APDS9960(i2c)
apds.enable_proximity = True
apds.enable_gesture = True
"""default gesture_proximity_threshold = 50 (range 0-255)"""
apds.gesture_proximity_threshold = 0
"""default gesture_gain = 2 (range 0-3)"""
apds.gesture_gain = 3
"""default gesture_fifo_threshold = 1 (range 0-3)"""
apds.gesture_fifo_threshold = 1
"""default gesture_dimensions = 1 (range 0-3)"""
apds.gesture_dimensions = 0
"""default rotation = 0 (possible, 0, 90, 180, 270)
90 sets green led to UP"""
apds.rotation = 90

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

while True:
    gesture = apds.gesture()

    if killswitch.value:
        if gesture == UP:
            mouse.move(0, 0, -3)
        elif gesture == DOWN:
            mouse.move(0, 0, 3)