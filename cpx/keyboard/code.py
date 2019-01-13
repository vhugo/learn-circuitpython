import time
import board
import neopixel

from digitalio import DigitalInOut, Direction, Pull

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

c1 = DigitalInOut(board.A7)
c1.direction = Direction.INPUT
c1.pull = Pull.UP
c2 = DigitalInOut(board.A1)
c2.direction = Direction.INPUT
c2.pull = Pull.UP
c3 = DigitalInOut(board.A2)
c3.direction = Direction.INPUT
c3.pull = Pull.UP
c4 = DigitalInOut(board.A3)
c4.direction = Direction.INPUT
c4.pull = Pull.UP
l1 = DigitalInOut(board.A6)
l1.direction = Direction.INPUT
l1.pull = Pull.UP
l2 = DigitalInOut(board.A5)
l2.direction = Direction.INPUT
l2.pull = Pull.UP
l3 = DigitalInOut(board.A4)
l3.direction = Direction.INPUT
l3.pull = Pull.UP
l4 = DigitalInOut(board.A0)
l4.direction = Direction.INPUT
l4.pull = Pull.UP

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.2)
pixels.fill((0, 0, 0))
pixels.show()

while True:
    if not c1.value and not l1.value:
        pixels.fill([50, 0, 0])
    elif not c1.value and not l2.value:
        pixels.fill([100, 0, 0])
    elif not c1.value and not l3.value:
        pixels.fill([150, 0, 0])
    elif not c1.value and not l4.value:
        pixels.fill([200, 0, 0])

    elif not c2.value and not l1.value:
        pixels.fill([0, 255, 0])
    elif not c2.value and not l2.value:
        pixels.fill([0, 255, 0])
    elif not c2.value and not l3.value:
        pixels.fill([0, 255, 0])
    elif not c2.value and not l4.value:
        pixels.fill([0, 255, 0])

    elif not c3.value and not l1.value:
        pixels.fill([255, 0, 0])
    elif not c3.value and not l2.value:
        pixels.fill([255, 0, 0])
    elif not c3.value and not l3.value:
        pixels.fill([255, 0, 0])
    elif not c3.value and not l4.value:
        pixels.fill([255, 0, 0])

    elif not c4.value and not l1.value:
        pixels.fill([255, 0, 0])
    elif not c4.value and not l2.value:
        pixels.fill([255, 0, 0])
    elif not c4.value and not l3.value:
        pixels.fill([255, 0, 0])
    elif not c4.value and not l4.value:
        pixels.fill([255, 0, 0])
    else:
        pixels.fill((0, 0, 0))


    time.sleep(0.01)
