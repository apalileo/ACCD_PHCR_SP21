"""
testing RCWL-1601 ultrasonic distance sensor (HC-SR04 compatible)
3.3V, GND, trigger to A1, echo to A2
"""

# import modules
import board
import time
import neopixel
import adafruit_hcsr04

# declare objects and variables
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.A1, echo_pin=board.A2)

# loop forever
while True:
    # sonar.distance outputs in cm, let's convert that to inches
    distInches = sonar.distance * 0.3937
    print(distInches)

    time.sleep(0.1)