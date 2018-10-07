# CircuitPython IO demo - analog output
import time
import board
from analogio import AnalogOut

analog_out = AnalogOut(board.A0)

while True:
    # Count up from 0 to 65535, with 64 increment
    # which ends up corresponding to the DAC's 10-bit range
    for i in range(30000, 40000, 64):
        analog_out.value = i
        time.sleep(0.01)

    for i in reversed(range(30000, 40000, 64)):
        analog_out.value = i
        time.sleep(0.01)
