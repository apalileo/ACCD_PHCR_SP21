"""Bench testing for PCHR 25/50 Lamp project"""

# import modules
import board
import time
import neopixel
import adafruit_hcsr04
from digitalio import DigitalInOut, Direction, Pull

# declare objects and variables

# STEMMA button
button = DigitalInOut(board.A3)
button.direction = Direction.INPUT
button.pull = Pull.DOWN
buttonPrev = True
buttonTime = 0

# indicator LEDs for Pomodoros
led25 = DigitalInOut(board.A4)
led25.direction = Direction.OUTPUT
led50 = DigitalInOut(board.A5)
led50.direction = Direction.OUTPUT

# ultrasonic sensor
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.A1, echo_pin=board.A2)

# onboard neopixels
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10,
                           brightness=0.2, auto_write=False)

# declare the lamp modes
lightMode = 0
LAMP_OFF = 0
LAMP_ON = 1
POMO_25 = 2
POMO_50 = 3
POMO_EXP = 4
POMO_BREAK = 5

# measure the distance of the user when starting a Pomodoro interval
userDist = 0
# the distance above the userDist for sensing user departure
userDistThresh = 6

# declare the color values
WHITE = (255, 255, 255)
BLUE = (125, 125, 255)
RED = (255, 125, 125)

# color assignment to pixels.fill()
color = 0

# loop forever
while True:

    # convert sonar.distance to inches
    distInches = sonar.distance * 0.3937

    # check for button press
    # button hold returns to LAMP_OFF
    if button.value != buttonPrev:
        buttonPrev = button.value
        if button.value is False:
            buttonTime = time.monotonic()
        else:
            if time.monotonic() >= buttonTime + 1:
                lightMode = LAMP_OFF
            else:
                lightMode += 1
                timeNow = time.monotonic()
                if lightMode > 3:
                    lightMode = 0

    if lightMode == LAMP_OFF:
        color = 0
        led25.value = False
        led50.value = False

    elif lightMode == LAMP_ON:
        color = WHITE
        led25.value = False
        led50.value = False

    elif lightMode == POMO_25:
        pomoInt = 5
        pomoBreak = 5
        led25.value = True
        led50.value = False
        color = BLUE
        if time.monotonic() >= timeNow + pomoInt:
            userDist = distInches
            lightMode = POMO_EXP

    # POMO_50 to be completed upon sorting of POMO_25
    elif lightMode == POMO_50:
        color = 0
        led25.value = False
        led50.value = True

    elif lightMode == POMO_EXP:
        color = WHITE
        if distInches >= userDist + userDistThresh:
            timeNow = time.monotonic()
            lightMode = POMO_BREAK

    elif lightMode == POMO_BREAK:
        color = RED
        if time.monotonic() >= timeNow + pomoBreak:
            lightMode = LAMP_ON

    pixels.fill(color)
    pixels.show()
    time.sleep(0.1)