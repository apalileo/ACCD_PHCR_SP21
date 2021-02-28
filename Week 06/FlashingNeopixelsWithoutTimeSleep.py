import time
from adafruit_circuitplayground import cp

flashInterval = 0.4
flashTime = time.monotonic() + flashInterval
WHITE = (50, 50, 50)
color = WHITE

while True:
    if time.monotonic() >= flashTime:
        if color == 0:
            color = WHITE
        elif color == WHITE:
            color = 0
        flashTime += flashInterval
    cp.pixels.fill(color)