import os
import time
import board
import busio
import digitalio
import gfx

from adafruit_rgb_display import ili9341, color565


def randrange(min_value, max_value):
    # Simple randrange implementation for ESP8266 uos.urandom function.
    # Returns a random integer in the range min to max.  Supports only 32-bit
    # int values at most.
    magnitude = abs(max_value - min_value)
    randbytes = os.urandom(4)
    offset = int((randbytes[3] << 24) | (randbytes[2] << 16) | (randbytes[1] << 8) | randbytes[0])
    offset %= (magnitude+1)  # Offset by one to allow max_value to be included.
    return min_value + offset


# Optionally create faster horizontal and vertical line drawing functions using
# the display's native filled rectangle function (which updates chunks of memory
# instead of pixel by pixel).
def fast_hline(x, y, width, color):
    display.fill_rectangle(x, y, width, 1, color)


def fast_vline(x, y, height, color):
    display.fill_rectangle(x, y, 1, height, color)


spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI, MISO=board.MISO)

# # For the ESP8266
# cs = digitalio.DigitalInOut(board.GPIO0)
# dc = digitalio.DigitalInOut(board.GPIO15)

# For the Feather M0s
cs = digitalio.DigitalInOut(board.D9)
dc = digitalio.DigitalInOut(board.D10)

display = ili9341.ILI9341(spi, cs=cs, dc=dc)

# Initialize the GFX library, giving it the display pixel function as its pixel
# drawing primitive command.  The hline and vline parameters specify optional
# optimized horizontal and vertical line drawing functions.  You can remove these
# to see how much slower the filled shape functions perform!
graphics = gfx.GFX(240, 320, display.pixel, hline=fast_hline, vline=fast_vline)

display.fill(0)  # Clear the display
graphics.line(0, 0, 239, 319, color565(255, 0, 0))

# Now loop forever drawing random lines.
display.fill(0)
while True:
    x0 = randrange(0, 240)
    y0 = randrange(0, 320)
    x1 = randrange(0, 240)
    y1 = randrange(0, 320)
    r = randrange(0, 255)
    g = randrange(0, 255)
    b = randrange(0, 255)
    graphics.line(x0, y0, x1, y1, color565(r, g, b))
    time.sleep(0.01)
