from adafruit_circuitplayground import cp
import time


while True:
    if cp.button_a:
        print("Button A pressed!")
        cp.red_led = False
        cp.pixels.fill(0xFF0000)
        cp.play_tone(1000, 0.5)

    if cp.button_b:
        print("Button B pressed!")
        cp.red_led = True
        cp.pixels.fill(0)

    time.sleep(0.1)
