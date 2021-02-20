# import modules
import board
from digitalio import DigitalInOut, Direction
import time

# declare objects and variables
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

# variables to control sleep time for blinking
onTime = 1.5
offTime = 1

# loop forever
while True:
    # turn the led on
    led.value = True
    time.sleep(onTime)
    # turn the led off
    led.value = False
    time.sleep(offTime)