import board
import busio
import time
from adafruit_apds9960.apds9960 import APDS9960

i2c = busio.I2C(board.SCL, board.SDA)
apds = APDS9960(i2c)
apds.enable_proximity = True
apds.enable_proximity_interrupt = True
apds.proximity_interrupt_threshold = (0, 175)

while True:
    print(apds.proximity)
    apds.clear_interrupt()

    time.sleep(0.1)