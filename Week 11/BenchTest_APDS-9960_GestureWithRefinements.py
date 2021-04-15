import board
import busio
import time
from adafruit_apds9960.apds9960 import APDS9960

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


while True:
    gesture = apds.gesture()

    if gesture == 0x01:
        print("up")
    elif gesture == 0x02:
        print("down")
    elif gesture == 0x03:
        print("left")
    elif gesture == 0x04:
        print("right")