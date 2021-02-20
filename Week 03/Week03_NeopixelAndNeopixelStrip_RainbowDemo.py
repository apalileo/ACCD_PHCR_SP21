# Circuit Playground NeoPixel
import time
import board
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.05,
                           auto_write=False)
pixelStrip = neopixel.NeoPixel(board.A1, 30, brightness=0.2,
                           auto_write=False)

rainbow_cycle_demo = 1

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(10):
            rc_index = (i * 256 // 10) + j * 5
            pixels[i] = wheel(rc_index & 255)
        for i in range(30):
            rcX_index = (i * 256 // 30) + j * 5
            pixelStrip[i] = wheel(rcX_index & 255)
        pixels.show()
        pixelStrip.show()
        time.sleep(wait)

while True:
    if rainbow_cycle_demo:
        rainbow_cycle(0.01)  # Increase the number to slow down the rainbow.