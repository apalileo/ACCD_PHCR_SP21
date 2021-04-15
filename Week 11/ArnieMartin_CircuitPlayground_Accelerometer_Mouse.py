# move your mouse cursor with the onboard accelerometer
# works with CPX and CPB, copy adafuit_hid to /lib

import board
import time
import digitalio
import busio
import adafruit_lis3dh
import usb_hid
from adafruit_hid.mouse import Mouse

i2c = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)
int1 = digitalio.DigitalInOut(board.ACCELEROMETER_INTERRUPT)
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x19, int1=int1)

mouse = Mouse(usb_hid.devices)

while True:
    x, y, z = lis3dh.acceleration

    if x > 2 or x < -2:
        mouse.move(x=int(-x))

    if y > 2 or y < -2:
        mouse.move(y=int(y))

    time.sleep(0.01)