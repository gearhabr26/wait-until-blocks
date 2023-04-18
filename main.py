how_long_is_the_circuit_broken_at_P0 = 0

def on_forever():
    global how_long_is_the_circuit_broken_at_P0
    if not (input.pin_is_pressed(TouchPin.P0)):
        basic.pause(20)
        how_long_is_the_circuit_broken_at_P0 += 20
        if how_long_is_the_circuit_broken_at_P0 > 1000:
            radio.send_number(1)
            WaitUntilBlocks.wait_until_button_pressed(Button.A)
    else:
        how_long_is_the_circuit_broken_at_P0 = 0
basic.forever(on_forever)
