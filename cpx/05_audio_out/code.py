"""
Basic tones

We first generate a single period of a sine wave in python, with the `math.sin`
function, and stick it into `sine_wave`.

Then we enable the speaker by setting the `SPEAKER_ENABLE` pin to be an output and
`True`.

We can create the audio object with this line that sets the output pin and the
sine wave sample object and give it the sample array

```
audio = audioio.AudioOut(board.SPEAKER)
sine_wave_sample = audioio.RawSample(sine_wave)
```

Finally you can run `audio.play()` - if you only want to play the sample once,
call as is. If you want it to loop the sample, which we definitely do so its one
long tone, pass in `loop=True`

You can then do whatever you like, the tone will play in the background until
you call `audio.stop()`

"""
import time
import array
import math
import audioio
import board
import digitalio

FREQUENCY = 440  # 440 Hz middle 'A'
SAMPLERATE = 8000  # 8000 samples/second, recommended!

# Generate one period of sine wav.
length = SAMPLERATE // FREQUENCY
sine_wave = array.array("H", [0] * length)
for i in range(length):
    sine_wave[i] = int(math.sin(math.pi * 2 * i / 18) * (2 ** 15) + 2 ** 15)

# enable the speaker
speaker_enable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speaker_enable.direction = digitalio.Direction.OUTPUT
speaker_enable.value = False

audio = audioio.AudioOut(board.A0)
sine_wave_sample = audioio.RawSample(sine_wave)

audio.play(sine_wave_sample, loop=True)  # keep playing the sample over and over
time.sleep(1)  # until...
audio.stop()  # we tell the board to stop

