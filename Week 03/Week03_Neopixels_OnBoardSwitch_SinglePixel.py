# import modules
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull
import time

# declare objects and variables
switch = DigitalInOut(board.SLIDE_SWITCH)
switch.direction = Direction.INPUT
switch.pull = Pull.UP
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.05,
                           auto_write=False)

# color variables
WHITE = (255, 255, 255)
OFF = (0, 0, 0)
currentColor = OFF

# loop forever
while True:
#     pixels.fill(currentColor)
    pixels[5] = currentColor
    pixels.show()
    if switch.value:
        currentColor = WHITE
    else:
        currentColor = OFF
    time.sleep(0.1)