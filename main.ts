let how_long_is_the_circuit_broken_at_P0 = 0
basic.forever(function () {
    if (!(input.pinIsPressed(TouchPin.P0))) {
        basic.pause(20)
        how_long_is_the_circuit_broken_at_P0 += 20
        if (how_long_is_the_circuit_broken_at_P0 > 1000) {
            radio.sendNumber(1)
            WaitUntilBlocks.waitUntilButtonPressed(Button.A)
        }
    } else {
        how_long_is_the_circuit_broken_at_P0 = 0
    }
})
