"""
Bench testing for PCHR 25/50 Lamp project
"""

# import modules
import board
import time
import neopixel
import adafruit_hcsr04
from digitalio import DigitalInOut, Direction, Pull

# declare objects and variables
button = DigitalInOut(board.A3)
button.direction = Direction.INPUT
button.pull = Pull.DOWN
buttonPrev = True

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.A1, echo_pin=board.A2)
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10,
                           brightness=0.2, auto_write=False)

lightMode = 0

# declare the color values
WHITE = (255, 255, 255)
BLUE = (125, 125, 255)
RED = (255, 125, 125)

# loop forever
while True:

    # sonar.distance outputs in cm, let's convert that to inches
    distInches = sonar.distance * 0.3937
    print(distInches)
    print(button.value)

    # check for button press
    if button.value != buttonPrev:
        buttonPrev = button.value
        if button.value is False:
            lightMode += 1
            if lightMode > 3:
                lightMode = 0

    # assign modes
    # mode 0 will be the OFF position
    if lightMode == 0:
        color =
    # mode 1 will be the standard lamp position
    elif lightMode == 1:
        color =
    # mode 2 will be the 25/5 Pomodoro interval
    elif lightMode == 2:
        color =
    # mode 3 will be the 50/10 Pomodoro interval
    elif lightMode == 3:
        color =

    pixels.fill(color)
    pixels.show()

    time.sleep(0.1)