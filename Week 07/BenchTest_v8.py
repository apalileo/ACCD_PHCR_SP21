"""
Bench testing for PCHR 25/50 Lamp project
Swapping out the STEMMA button and the potentiometer with a rotary encoder
"""

# import modules
import board
import time
import rotaryio
import adafruit_hcsr04
from digitalio import DigitalInOut, Direction, Pull
from adafruit_circuitplayground import cp

# declare objects and variables

# rotary encoder button
button = DigitalInOut(board.A3)
button.direction = Direction.INPUT
button.pull = Pull.UP
buttonPrev = True
buttonTime = 0

# rotary encoder knob
knob = rotaryio.IncrementalEncoder(board.A6, board.TX)
knobPrev = knob.position

# indicator LEDs for Pomodoros
led25 = DigitalInOut(board.A4)
led25.direction = Direction.OUTPUT
led50 = DigitalInOut(board.A5)
led50.direction = Direction.OUTPUT

# ultrasonic sensor
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.A1, echo_pin=board.A2)

# declare the lamp modes
lightMode = 0
LAMP_OFF = 0
LAMP_ON = 1
POMO_25 = 2
POMO_50 = 3
POMO_EXP = 4
POMO_BREAK = 5
POMO_LONG_BREAK = 6

# measure the total number of Pomodoro intervals
pomoTotal = 0

# measure the distance of the user when starting a Pomodoro interval
userDist = 0
# the distance above the userDist for sensing user departure
userDistThresh = 6

# the color values
WHITE = (255, 255, 255)
BLUE = (125, 125, 255)
ORANGE = (255, 125, 0)
RED = (255, 100, 100)

# brightness variable for controlling
pixelBrightness = 0.2

# flashing the neopixels on Pomodoro interval end
flashInterval = 0.3

# loop forever
while True:

    # convert sonar.distance to inches
    distInches = sonar.distance * 0.3937

    # preventing button press from registering during flash or break
    if lightMode != POMO_EXP and lightMode != POMO_BREAK:
        # check for button press
        if button.value != buttonPrev:
            buttonPrev = button.value
            if button.value is False:
                buttonTime = time.monotonic()
            else:
                # button hold returns to LAMP_OFF
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
        pomoBreak = 2.5
        led25.value = True
        led50.value = False
        color = BLUE
        if time.monotonic() >= timeNow + pomoInt:
            flashTime = time.monotonic() + flashInterval
            userDist = distInches
            pomoTotal += 0.5
            lightMode = POMO_EXP

    elif lightMode == POMO_50:
        pomoInt = 10
        pomoBreak = 5
        led25.value = False
        led50.value = True
        color = BLUE
        if time.monotonic() >= timeNow + pomoInt:
            flashTime = time.monotonic() + flashInterval
            userDist = distInches
            pomoTotal += 1
            lightMode = POMO_EXP

    elif lightMode == POMO_EXP:
        if time.monotonic() >= flashTime:
            if color == 0:
                color = BLUE
            elif color == BLUE:
                color = 0
            flashTime += flashInterval
        elif distInches >= userDist + userDistThresh:
            timeNow = time.monotonic()
            if pomoTotal >= 2:
                lightMode = POMO_LONG_BREAK
            else:
                lightMode = POMO_BREAK

    elif lightMode == POMO_BREAK:
        color = ORANGE
        if time.monotonic() >= timeNow + pomoBreak:
            lightMode = LAMP_ON

    elif lightMode == POMO_LONG_BREAK:
        color = RED
        pomoBreak = 15
        if time.monotonic() >= timeNow + pomoBreak:
            pomoTotal = 0
            lightMode = LAMP_ON

    # adjusting brightness based on rotary input
    if knob.position > knobPrev:
        knobPrev = knob.position
        if pixelBrightness >= 1.00:
            pixelBrightness = 1.00
        else:
            pixelBrightness += 0.10

    # cap the minimum brightness at 0.20
    if knob.position < knobPrev:
        knobPrev = knob.position
        if pixelBrightness <= 0.20:
            pixelBrightness = 0.20
        else:
            pixelBrightness -= 0.10

    cp.pixels.fill(color)
    cp.pixels.show()
    cp.pixels.brightness = pixelBrightness
    time.sleep(0.1)