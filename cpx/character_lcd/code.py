import time
import board
import digitalio
import adafruit_character_lcd

lcd_rs = digitalio.DigitalInOut(board.A6)
lcd_en = digitalio.DigitalInOut(board.A5)
lcd_d7 = digitalio.DigitalInOut(board.A2)
lcd_d6 = digitalio.DigitalInOut(board.A1)
lcd_d5 = digitalio.DigitalInOut(board.A3)
lcd_d4 = digitalio.DigitalInOut(board.A4)

lcd_columns = 16
lcd_rows = 2

lcd = adafruit_character_lcd.Character_LCD(lcd_rs, lcd_en, lcd_d4, lcd_d5,
					   lcd_d6, lcd_d7, lcd_columns,
					   lcd_rows)

#   Print a 2x line message
lcd.message('hello\ncircuitpython')

# Wait 5s
time.sleep(5)

#   Demo showing cursor
lcd.clear()
lcd.show_cursor(True)
lcd.message('showing cursor ')

#   Wait 5s
time.sleep(5)

#   Demo showing the blinking cursor
lcd.clear()
lcd.blink(True)
lcd.message('Blinky Cursor!')

#   Wait 5s
time.sleep(5)
lcd.blink(False)

#   Demo scrolling message LEFT
lcd.clear()
scroll_msg = 'Scroll'
lcd.message(scroll_msg)

#   Scroll to the left
for i in range(lcd_columns - len(scroll_msg)):
    time.sleep(0.5)
    lcd.move_left()

lcd.clear()
lcd.message("going to sleep\ncya later!")
time.sleep(2)
lcd.enable_display(False)
