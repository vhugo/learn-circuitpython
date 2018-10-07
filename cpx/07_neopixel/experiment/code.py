import time

import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull

RED = (0x10, 0, 0)
YELLOW = (0x10, 0x10, 0)
GREEN = (0, 0x10, 0)
AQUA = (0, 0x10, 0x10)
BLUE = (0, 0, 0x10)
PURPLE = (0x10, 0, 0x10)
BLACK = (0, 0, 0)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.1)
pixels.fill((0, 0, 0))
pixels.show()

switch = DigitalInOut(board.SLIDE_SWITCH)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

buttonA = DigitalInOut(board.BUTTON_A)
buttonA.direction = Direction.INPUT
buttonA.pull = Pull.DOWN

buttonB = DigitalInOut(board.BUTTON_B)
buttonB.direction = Direction.INPUT
buttonB.pull = Pull.DOWN

colors = [RED, YELLOW, GREEN, AQUA, BLUE, PURPLE]
colorn = ["RED", "YELLOW", "GREEN", "AQUA", "BLUE", "PURPLE"]
color = BLACK

while True:

    commands = [
        (switch.value and buttonA.value and buttonB.value),
        (switch.value and buttonA.value and not buttonB.value),
        (switch.value and not buttonA.value and buttonB.value),
        (not switch.value and buttonA.value and buttonB.value),
        (not switch.value and buttonA.value and not buttonB.value),
        (not switch.value and not buttonA.value and buttonB.value)
    ]

    for idx, cmd in enumerate(commands):
        if cmd:
            if color == colors[idx]:
                color = BLACK
                print('%d is deactive color: BLACK' % idx)

            else:
                color = colors[idx]
                print('%d is active color: %s' % (idx, colorn[idx]))

            for led_idx, led in enumerate(pixels):
                pixels[led_idx] = color
                time.sleep(.05)

