# import time
# from adafruit_circuitplayground import cp

# cp.detect_taps = 2
# tap_count = 0



# while True:
#     x, y, z = cp.acceleration
#     print((x, y, z))

#     if cp.tapped:
#         tap_count += 1
#         print("TAP!", tap_count)

#     if cp.shake():
#         print("SHOOKEN!")

#     time.sleep(0.1)

"""If the switch is to the right, it will appear that nothing is happening. Move the switch to the
left to see the NeoPixels light up in colors related to the accelerometer! The Circuit Playground
has an accelerometer in the center that returns (x, y, z) acceleration values. This program uses
those values to light up the NeoPixels based on those acceleration values."""

from adafruit_circuitplayground import cp
import time

# Main loop gets x, y and z axis acceleration, prints the values, and turns on
# red, green and blue, at levels related to the x, y and z values.
while True:
    if not cp.switch:
        # If the switch is to the right, it returns False!
        print("Slide switch off!")
        cp.pixels.fill((0, 0, 0))
        time.sleep(0.1)
        continue
    R = 0
    G = 0
    B = 0
    x, y, z = cp.acceleration
#     print((x, y, z))
    cp.pixels.fill(((R + abs(int(x))), (G + abs(int(y))), (B + abs(int(z)))))

    print(cp.sound_level)

    time.sleep(0.1)