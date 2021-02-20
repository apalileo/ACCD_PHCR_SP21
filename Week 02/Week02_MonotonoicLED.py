# import modules
import board
import time
from digitalio import DigitalInOut, Direction

# declare objects and variables
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

blinkInterval = 1
blinkTime = time.monotonic() + blinkInterval

# loop forever
while True:

    # check if it is time to change the led
    if time.monotonic() >= blinkTime:

        # print debug to the serial monitor
        print("Time to change the led")
        print(blinkTime)

        # toggle led value
        led.value = not led.value

        # print the new led value
        print(led.value)

        # increment the blinkTime by blinkInterval
        blinkTime += blinkInterval

        # print new blinkTime
        print(blinkTime)