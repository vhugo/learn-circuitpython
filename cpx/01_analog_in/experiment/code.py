""" CircuitPlaygroundExpress_AnalogIn
reads the analog voltage level from a 10k potentiometer
connected to GND, 3.3V, and pin A1
and prints the results to the REPL
"""

import time

import board
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

analogin = AnalogIn(board.A1)


def get_voltage(pin):  # helper
    """
     Converts the 0-65535 reading from pin.value and convert it a 0-3.3V
     voltage reading. By default, analog readings will range from 0 (minimum)
     to 65535 (maximum).
    """
    return (pin.value * 3.3) / 65536


while True:
    led.value = True
    time.sleep(0.1)
    led.value = False

    frequency = get_voltage(analogin)
    print("Analog Voltage: %f" % frequency)
    time.sleep(frequency)

