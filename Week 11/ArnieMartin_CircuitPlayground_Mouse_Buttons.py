
# use onboard buttons to control LMB and RMB
# works with CPX and CPB, copy adafuit_hid to /lib

import board
import time
import digitalio
import busio
import adafruit_lis3dh
import usb_hid
from adafruit_hid.mouse import Mouse

lmb = digitalio.DigitalInOut(board.BUTTON_A)
lmb.direction = digitalio.Direction.INPUT
lmb.pull = digitalio.Pull.DOWN
lmb_pre = lmb.value

rmb = digitalio.DigitalInOut(board.BUTTON_B)
rmb.direction = digitalio.Direction.INPUT
rmb.pull = digitalio.Pull.DOWN
rmb_pre = rmb.value

mouse = Mouse(usb_hid.devices)

while True:

    if rmb.value:
        mouse.press(Mouse.RIGHT_BUTTON)
    else:
        mouse.release(Mouse.RIGHT_BUTTON)


    if lmb.value:
        mouse.press(Mouse.LEFT_BUTTON)
    else:
        mouse.release(Mouse.LEFT_BUTTON)