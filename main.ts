input.onButtonPressed(Button.A, function () {
    Alarm = 0
    strip.showColor(neopixel.colors(NeoPixelColors.Green))
})
let Noise = 0
let Alarm = 0
let strip: neopixel.Strip = null
strip = neopixel.create(DigitalPin.P8, 1, NeoPixelMode.RGB)
Alarm = 0
strip.showColor(neopixel.colors(NeoPixelColors.Red))
basic.pause(1000)
strip.showColor(neopixel.colors(NeoPixelColors.Green))
basic.pause(1000)
basic.showIcon(IconNames.Yes)
basic.pause(1000)
basic.clearScreen()
basic.forever(function () {
    Noise = smarthome.ReadNoise(AnalogPin.P2)
})
basic.forever(function () {
    if (Alarm == 0) {
        basic.showNumber(Noise)
    } else {
        basic.showIcon(IconNames.No)
    }
})
basic.forever(function () {
    if (Alarm == 1) {
        strip.showColor(neopixel.colors(NeoPixelColors.Red))
        music.playTone(262, music.beat(BeatFraction.Whole))
    }
})
basic.forever(function () {
    if (Noise >= 100) {
        Alarm = 1
    }
})
