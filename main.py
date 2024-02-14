def ledtoggleAll():
    pass
led.toggleAll()
def on_button_pressed_a():
    led.enable(True)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    led.enable(False)
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_leds("""
    . # # # .
    # . # . #
    # # . # #
    # . # . #
    . # # # .
    """)

def on_forever():
    ledtoggleAll()
    basic.pause(500)
basic.forever(on_forever)
