# import modules
import board
import time
from digitalio import DigitalInOut, Direction

# declare objects and variables
switch = DigitalInOut(board.A1)
switch.direction = Direction.INPUT
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

# variables to control sleep time for blinking


# loop forever
while True:
    # print switch.value to the serial monitor
    print(switch.value)

    # write the switch value to the led
    led.value = switch.value

    # pause a bit
    time.sleep(0.1)