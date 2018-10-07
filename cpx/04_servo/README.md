[CircuitPython Servo](https://learn.adafruit.com/adafruit-circuit-playground-express/circuitpython-servo)

In order to use servos, we take advantage of `pulseio`. Now, in theory, you could
just use the raw pulseio calls to set the frequency to 50 Hz and then set the
pulse widths. But we would rather make it a little more elegant and easy!

So, instead we will use `adafruit_motor` which manages servos for you quite
nicely! `adafruit_motor` is a library so be sure to (grab it from the library
bundle)[https://github.com/adafruit/Adafruit_CircuitPython_Bundle] if you have
not yet! If you need help installing the library, check out the CircuitPython
Libraries page.

To use the bundle download the zip (not source zip) from the (latest
release)[https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/latest],
unzip it and copy over the subfolders, such as lib, into the root of your
CircuitPython device. Make sure to indicate that it should be merged with the
existing folder when it exists.

The libraries in each release are compiled for all recent major versions of
CircuitPython. Please download the one that matches the major version of your
CircuitPython. For example, if you are running 3.0.0 you should download the 3.x
bundle.

