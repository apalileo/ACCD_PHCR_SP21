# import modules
import board
import time
from digitalio import DigitalInOut, Direction, Pull

# declare objects and variables
led = DigitalInOut(board.A3)
led.direction = Direction.OUTPUT

button = DigitalInOut(board.A1)
button.direction = Direction.INPUT
button.pull = Pull.DOWN

blinkInterval = 0.5
blinkTime = time.monotonic() + blinkInterval

# loop forever
while True:
    # check the button state
    if button.value:

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