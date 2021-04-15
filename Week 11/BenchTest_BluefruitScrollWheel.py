"""
Circuit Playground Bluefruit onboard buttons as scroll wheel

Killswitch and button assignments from Arnie Martin's
CircuitPlayground_Mouse_Buttons.py
https://gist.github.com/RealAbsurdity/ed00a16b342994796a49fb57aaa8ae6b

Adafruit HID Library referenced for mouse
https://circuitpython.readthedocs.io/projects/hid/en/latest/
"""

import board
import time
import digitalio
import busio
import adafruit_lis3dh
import usb_hid
from adafruit_hid.mouse import Mouse

killswitch = digitalio.DigitalInOut(board.SLIDE_SWITCH)
killswitch.direction = digitalio.Direction.INPUT
killswitch.pull = digitalio.Pull.UP

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

    if killswitch.value:

        if rmb.value:
            mouse.move(0, 0, 1)

        if lmb.value:
            mouse.move(0, 0, -1)