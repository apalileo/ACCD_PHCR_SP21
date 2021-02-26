# import modules
import board
import time
import touchio
import neopixel

# declare objects and variables
# declare touchIn object on CPE cap-touch pin (A1 - A6 and TX)
touchPin1 = touchio.TouchIn(board.A1)
touchPin2 = touchio.TouchIn(board.A2)
touchPin3 = touchio.TouchIn(board.A3)
touchPin4 = touchio.TouchIn(board.A4)
touchPin5 = touchio.TouchIn(board.A5)
touchPin6 = touchio.TouchIn(board.A6)
touchPin7 = touchio.TouchIn(board.TX)
touchPre = touchPin1.value

# neopixel stuff
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.05,
                           auto_write=False)
color = [255, 255, 255]

toggleLED = False

# repeat forever
while True:
    # capture touch input
    if touchPin1.value != touchPre:
        touchPre = touchPin1.value
        if touchPin1.value:
            toggleLED = not toggleLED

    if toggleLED:
        pixels.fill(color)
        pixels.show()

        if touchPin2.value and touchPin3.value:
            if color[0] >= 245:
                incrementR = -10
            if color[0] <= 10:
                incrementR = 10
            color[0] += incrementR

        if touchPin4.value and touchPin5.value:
            if color[1] >= 245:
                incrementG = -10
            if color[1] <= 10:
                incrementG = 10
            color[1] += incrementG

        if touchPin6.value and touchPin7.value:
            if color[2] >= 245:
                incrementB = -10
            if color[2] <= 10:
                incrementB = 10
            color[2] += incrementB

    else:
        pixels.fill(0)
        pixels.show()
        # reset to white
        for i in range(3):
            color[i] = 255

    time.sleep(0.1)