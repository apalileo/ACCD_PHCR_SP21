
# more advanced-ish use of single onboard button to control LMB and RMB
# works with CPX and CPB, copy adafuit_hid to /lib

import board
import time
import digitalio
import busio
import adafruit_lis3dh
import usb_hid
from adafruit_hid.mouse import Mouse

killswitch = digitalio.DigitalInOut(board.SLIDE_SWITCH)
killswitch.direction = digitalio.Direction.INPUT
killswitch.pull = digitalio.Pull.UP

smb = digitalio.DigitalInOut(board.BUTTON_A)
smb.direction = digitalio.Direction.INPUT
smb.pull = digitalio.Pull.DOWN
smb_pre = smb.value

mouse = Mouse(usb_hid.devices)

smb_time = 0
RMB_DELAY = 0.5

while True:

    if killswitch.value:
        if smb.value is not smb_pre:
            smb_pre = smb.value
            if smb.value:
                print("button clicked...")
                smb_time = time.monotonic()
                print("press time is", smb_time)
            if not smb.value:
                print("release time is", time.monotonic())
                eltime = time.monotonic() - smb_time
                print("elapsed time is", eltime)
                if eltime < RMB_DELAY:
                    print("short press... LMB clicked!")
                    mouse.click(Mouse.LEFT_BUTTON)
                    smb_time = 0
        else:
            if smb_time != 0:
                eltime = time.monotonic() - smb_time
                print("elapsed time is", eltime)
                time.sleep(0.01)
                if eltime > RMB_DELAY:
                    print("long press... RMB clicked!")
                    mouse.click(Mouse.RIGHT_BUTTON)
                    smb_time = 0