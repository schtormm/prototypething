def on_pin_pressed_p1():
    basic.show_number(actual_time)
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

actual_time = 0
_4digit = grove.create_display(DigitalPin.P0, DigitalPin.P14)
timeanddate.set_time(12, 25, 0, timeanddate.MornNight.PM)

def on_forever():
    
    def on_numeric_time(hour, minute, second, month, day, year):
        global actual_time
        actual_time2 = int("" + str(minute) + ("" + str(second)))
    timeanddate.numeric_time(on_numeric_time)
    
    _4digit.show(actual_time)
    basic.pause(500)
    timeanddate.advance_by(0, timeanddate.TimeUnit.MILLISECONDS)
basic.forever(on_forever)
