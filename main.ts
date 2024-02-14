function ledtoggleAll () {
    led.toggleAll()
}
input.onButtonPressed(Button.A, function () {
    led.enable(true)
})
input.onButtonPressed(Button.B, function () {
    led.enable(false)
})
basic.showLeds(`
    . # # # .
    # . # . #
    # # . # #
    # . # . #
    . # # # .
    `)
basic.forever(function () {
    ledtoggleAll()
    basic.pause(500)
})
