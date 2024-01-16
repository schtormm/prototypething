goOff = False
actual_time = 0
_4digit = grove.create_display(DigitalPin.P0, DigitalPin.P14)
timeanddate.set24_hour_time(12, 25, 0)
def on_forever():
    global actual_time
    
    if goOff == True:
        pass
    def onNumeric_time(hour, minute, second, month, day, year):
        actual_time = int(str(hour) + str(minute))
    timeanddate.numeric_time(onNumeric_time)
    
    _4digit.show()
    basic.pause(500)
    timeanddate.advance_by(-1, timeanddate.TimeUnit.SECONDS)
basic.forever(on_forever)

def on_pin_pressed_p1():
    global goOf
    goOff = True
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)
