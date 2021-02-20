# import modules
import board
import time
from digitalio import DigitalInOut, Direction, Pull

# declare objects and variables
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

button = DigitalInOut(board.SLIDE_SWITCH)
button.direction = Direction.INPUT
button.pull = Pull.UP

# variables to control sleep time for blinking


# loop forever
while True:
    # print button.value to the serial monitor
    print(button.value)

    # write the button value to the led
    led.value = button.value

    # pause a bit
    time.sleep(0.1)