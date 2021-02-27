import time
import board
import analogio
# import adafruit_thermistor
from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService
from adafruit_circuitplayground import cp

ble = BLERadio()
uart_server = UARTService()
advertisement = ProvideServicesAdvertisement(uart_server)

# thermistor = adafruit_thermistor.Thermistor(board.TEMPERATURE,
#                                             10000, 10000, 25, 3950)
# light = analogio.AnalogIn(board.LIGHT)


def scale(value):
    """Scale the light sensor values from 0-65535 (AnalogIn range)
    to 0-50 (arbitrarily chosen to plot well with temperature)"""
    return value / 65535 * 50


while True:
    # Advertise when not connected.
    ble.start_advertising(advertisement)
    while not ble.connected:
        pass
    ble.stop_advertising()

    while ble.connected:
        if cp.button_a:
            print("Button A pressed!")
            cp.red_led = False
            cp.pixels.fill(0xFF0000)
            cp.play_tone(1000, 0.5)
            b_a = 100
        else:
            b_a = 0

        if cp.button_b:
            print("Button B pressed!")
            cp.red_led = True
            cp.pixels.fill(0)
            b_b = 100
        else:
            b_b = 0

        time.sleep(0.1)
        print((cp.light, cp.temperature, b_a, b_b))
        uart_server.write("{}, {}, {}, {}\n".format(cp.light, cp.temperature, b_a, b_b))
        time.sleep(0.1)