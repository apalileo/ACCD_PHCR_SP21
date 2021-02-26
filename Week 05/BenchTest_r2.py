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

led25 = DigitalInOut(board.A4)
led25.direction = Direction.OUTPUT
led50 = DigitalInOut(board.A5)
led50.direction = Direction.OUTPUT

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.A1, echo_pin=board.A2)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10,
                           brightness=0.2, auto_write=False)

lightMode = 0

# declare the color values
WHITE = (255, 255, 255)
BLUE = (125, 125, 255)
RED = (255, 125, 125)

# declare interaction variables
# measure the distance of the user when starting a Pomodoro interval
userDist = 0
# the distance above the userDist for sensing user departure
userDistThresh = 6
# Pomodoro intervals
pomoInt25 = 5
pomoInt50 = 10

def flash_neopixels():
    pixels.fill(0)
    pixels.show()
    time.sleep(0.2)
    pixels.fill(BLUE)
    pixels.show()
    time.sleep(0.2)

# loop forever
while True:

    # sonar.distance outputs in cm, let's convert that to inches
    distInches = sonar.distance * 0.3937

    # check for button press
    if button.value != buttonPrev:
        buttonPrev = button.value
        if button.value is False:
            # advance lightMode
            lightMode += 1
            # record the time when the button is pressed
            timeNow = time.monotonic()
            # record the distance to the user when the button is pressed
            userDist = distInches
            # reset the lightMode
            if lightMode > 3:
                lightMode = 0

    # assign modes
    # mode 0 is off
    if lightMode == 0:
        led50.value = False
        pixels.fill(0)
        pixels.show()

    # mode 1 is lamp only
    if lightMode == 1:
        pixels.fill(WHITE)
        pixels.show()

    # mode 2 is the 25/5 Pomodoro interval
    if lightMode == 2:
        led25.value = True
        pixels.fill(BLUE)
        pixels.show()
        if time.monotonic() >= timeNow + pomoInt25:
            if distInches <= userDist + userDistThresh:
                flash_neopixels()
            else:
                pixels.fill(RED)
                pixels.show()
        time.sleep(0.1)

    # mode 3 is the 50/10 Pomodoro interval
    if lightMode == 3:
        led25.value = False
        led50.value = True
        pixels.fill(BLUE)
        pixels.show()
        if time.monotonic() >= timeNow + pomoInt50:
            if distInches <= userDist + userDistThresh:
                flash_neopixels()
            else:
                pixels.fill(RED)
                pixels.show()

        time.sleep(0.1)

    time.sleep(0.1)