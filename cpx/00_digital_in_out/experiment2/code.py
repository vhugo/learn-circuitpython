# CircuitPlaygroundExpress_DigitalIO

import time

import board
from digitalio import DigitalInOut, Direction, Pull

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

buttonA = DigitalInOut(board.BUTTON_A)
buttonA.direction = Direction.INPUT
buttonA.pull = Pull.DOWN

buttonB = DigitalInOut(board.BUTTON_B)
buttonB.direction = Direction.INPUT
buttonB.pull = Pull.DOWN

while True:
    if buttonA.value and buttonB.value:  # button is pushed
        led.value = True
    else:
        led.value = False

    time.sleep(0.01)

