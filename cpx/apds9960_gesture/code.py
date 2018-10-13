import board
import busio
import neopixel

from adafruit_apds9960.apds9960 import APDS9960

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.2)
pixels.fill((0, 0, 0))
pixels.show()

i2c = busio.I2C(board.SCL, board.SDA)

apds = APDS9960(i2c)
apds.enable_gesture = True
apds.enable_proximity = True

while True:
    gesture = apds.gesture()

    if gesture == 0x01:
        pixels.fill([255, 0, 0])

    elif gesture == 0x02:
        pixels.fill([0, 255, 0])

    elif gesture == 0x03:
        pixels.fill([0, 0, 255])

    elif gesture == 0x04:
        pixels.fill([0, 255, 255])

    apds.clear_interrupt()

