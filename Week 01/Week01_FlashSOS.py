# import modules
import board
from digitalio import DigitalInOut, Direction
import time

# declare objects and variables
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

# variables to control sleep time for blinking
sOnTime = 0.20
oOnTime = 1.00
offTime = 0.20
pauseTime = 0.50
breakTime = 2.00

# loop forever
while True:
    for i in range(3):
        # turn the led on
        led.value = True
        time.sleep(sOnTime)
        # turn the led off
        led.value = False
        time.sleep(offTime)
    time.sleep(pauseTime)
    for i in range(3):
        # turn the led on
        led.value = True
        time.sleep(oOnTime)
        # turn the led off
        led.value = False
        time.sleep(offTime)
    time.sleep(pauseTime)
    for i in range(3):
        # turn the led on
        led.value = True
        time.sleep(sOnTime)
        # turn the led off
        led.value = False
        time.sleep(offTime)
    time.sleep(breakTime)