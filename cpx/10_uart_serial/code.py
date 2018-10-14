# CircuitPython Demo - USB/Serial echo

import board
import busio
import digitalio

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

buttonA = digitalio.DigitalInOut(board.BUTTON_A)
buttonA.direction = digitalio.Direction.INPUT

buttonB = digitalio.DigitalInOut(board.BUTTON_B)
buttonB.direction = digitalio.Direction.INPUT

uart = busio.UART(board.TX, board.RX, baudrate=9600)

while True:
    if buttonA.value:
        led.value = True
        uart.write("1")

    if buttonB.value:
        led.value = False
        uart.write("0")

