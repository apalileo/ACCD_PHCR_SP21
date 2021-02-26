# Anthony Palileo - Prototype: Hack. Code. Repeat. - Spring 2021

# this sketch runs on the Bluefruit board along with two potentiometers. One is
# attached at A1 and the other at A2. Ideally, the potentiometer values
# INCREASE as they are turned clockwise. If the full stops are situated at the
# top (12 o'clock) position, that would be ideal. The Bluefruit board should be
# situated with the USB port at the top (12 o'clock) position.

# neopixel.mpy and simpleio.mpy must be in the Lib folder of the board's memory


# import modules
import board
import analogio
import simpleio
from digitalio import DigitalInOut, Direction, Pull
import neopixel
import time

# declare objects and variables

# two potentiometers
pot1 = analogio.AnalogIn(board.A1)
pot2 = analogio.AnalogIn(board.A2)

# onboard switch
switch = DigitalInOut(board.SLIDE_SWITCH)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

# onboard button A
buttonA = DigitalInOut(board.BUTTON_A)
buttonA.direction = Direction.INPUT
buttonA.pull = Pull.DOWN
buttonA_prev = buttonA.value

# onboard button B
buttonB = DigitalInOut(board.BUTTON_B)
buttonB.direction = Direction.INPUT
buttonB.pull = Pull.DOWN
buttonB_prev = buttonB.value

# defining the brightness to include it in the pixel definition
currentBrightness = 0.0

# onboard Neopixels (line break because it was too long)
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10,
                           brightness=currentBrightness, auto_write=False)

# color and related variables
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (255, 65, 0)
YELLOW = (255, 200, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
OFF = (0, 0, 0)

colorVal = [WHITE, RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]
colorMode = 0

currentPixel = 0


# function for getting voltage from the potentiometers
def get_voltage(pin):
    return (pin.value * 3.3) / 65536

# loop forever
while True:
    # get the potentiometer inputs
    pot1Voltage = get_voltage(pot1)
    pot2Voltage = get_voltage(pot2)

    # map the input of pot1 to determine which led to light up
    # mapped in reverse to coordinate with physical led locations on board
    currentPixel = round(simpleio.map_range(pot1Voltage, 0, 3.3, 9, 0))

    # map the input of pot2 to determine the brightness of the led
    currentBrightness = simpleio.map_range(pot2Voltage, 0, 3.3, 0.01, 1)

    # check the slider is in the ON position
    # in this case I prefer right for the ON position, so if False
    if switch.value is False:

        # do the led stuff
        pixels[currentPixel] = colorVal[colorMode]
        pixels.show()
        pixels.brightness = currentBrightness
        # turn on only one led based on the potentiometer input
        for i in range(10):
            if i == currentPixel:
                pixels[currentPixel] = colorVal[colorMode]
            else:
                pixels[i] = OFF

        # check for on-board button presses
        # left button scrolls down the list
        if buttonA.value != buttonA_prev:
            buttonA_prev = buttonA.value
            if buttonA.value:
                colorMode -= 1
                if colorMode < 0:
                    colorMode = 6
        # right button scrolls up the list
        if buttonB.value != buttonB_prev:
            buttonB_prev = buttonB.value
            if buttonB.value:
                colorMode += 1
                if colorMode > 6:
                    colorMode = 0

    # if the slider is set to left (True)
    else:
        # turn off the led
        pixels.fill(0)
        pixels.show()

        # reset the color to white
        colorMode = 0

    time.sleep(0.1)