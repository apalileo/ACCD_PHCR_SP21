# import modules
import board
import time
from digitalio import DigitalInOut, Direction, Pull

# declare objects and variables
led = DigitalInOut(board.A3)
led.direction = Direction.OUTPUT
ledMode = 0

button = DigitalInOut(board.A1)
button.direction = Direction.INPUT
button.pull = Pull.DOWN
buttonPre = False

blinkInterval = 0.5
blinkTime = time.monotonic() + blinkInterval

# loop forever
while True:
    # gather inputs

    # see if the button has changed
    if button.value != buttonPre:
        # reset the previous value
        buttonPre = button.value
        if button.value:
            ledMode += 1
            if ledMode > 1:
                ledMode = 0

    # do output based on mode
    if ledMode == 1:
        # is it time to toggle the led?
        if time.monotonic() >= blinkTime:
            # blink
            print("blink")
            # toggle led value
            led.value = not led.value
            # increment the blinkTime
            blinkTime += blinkInterval

    else:
        led.value = False
        blinkTime = time.monotonic()