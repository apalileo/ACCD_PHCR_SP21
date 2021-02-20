# import modules
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull
import time

# declare objects and variables
switch = DigitalInOut(board.SLIDE_SWITCH)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

buttonA = DigitalInOut(board.BUTTON_A)
buttonA.direction = Direction.INPUT
buttonA.pull = Pull.DOWN
buttonAPre = False

buttonB = DigitalInOut(board.BUTTON_B)
buttonB.direction = Direction.INPUT
buttonB.pull = Pull.DOWN
buttonBPre = False

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.05,
                           auto_write=False)

# color variables
OFF = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 35, 0)
BLUE = (0, 0, 255)
currentColor = OFF
colorMode = 0

# loop forever
while True:
    pixels.fill(currentColor)
    pixels.show()
    if switch.value:
        # test for colorMode to determine output
        if colorMode == 1:
            currentColor = ORANGE
        elif colorMode == 2:
            currentColor = BLUE
        else:
            currentColor = WHITE

        # test for button presses
        if buttonA.value != buttonAPre:
            # reset the value
            buttonAPre = buttonA.value
            colorMode = 1
        if buttonB.value != buttonBPre:
            # reset the value
            buttonBPre = buttonB.value
            colorMode = 2
    else:
        currentColor = OFF
        colorMode = 0
    time.sleep(0.1)