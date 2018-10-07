# CircuitPlaygroundExpress_DigitalIO

import time

import board
from digitalio import DigitalInOut, Direction, Pull

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

switch = DigitalInOut(board.SLIDE_SWITCH)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

while True:
    if switch.value:  # switch is slid to the left
        led.value = True
    else:
        led.value = False

    time.sleep(0.01)

