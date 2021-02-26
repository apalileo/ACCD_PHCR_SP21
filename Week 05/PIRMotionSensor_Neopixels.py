"""
testing PIR Motion sensor attached at VOUT, GND, and A2
confirmation of movement lights up Neopixel array
"""


# import modules
import board
import neopixel
from digitalio import DigitalInOut, Direction

# declare objects and variables
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
WHITE = (10, 10, 10)

pirMotion = DigitalInOut(board.A2)
pirMotion.direction = Direction.INPUT

pirMotionPrev = pirMotion.value

# loop forever
while True:
    pirMotionVal = pirMotion.value
    if pirMotionVal:
        pixels.fill(WHITE)
    else:
        pixels.fill(0)