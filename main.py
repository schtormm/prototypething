goOff = False
actual_time = 0;
Display: grove.TM1637 = None
Display = grove.create_display(DigitalPin.P0, DigitalPin.P14)
timeanddate.set24_hour_time(12, 25, 0)
def on_forever():
    global _4digit
    
    if goOff == True:
        pass
    def onNumeric_time(hour, minute, second, month, day, year):
        actual_time = parse_int(str(hour) + str(minute))
    timeanddate.numeric_time(onNumeric_time)
    
    Display.show(actual_time)
    basic.pause(5000)
    timeanddate.advance_by(-1, timeanddate.TimeUnit.SECONDS)
basic.forever(on_forever)

def on_pin_pressed_p1():
    global goOf
    goOff = True
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)
