def on_button_pressed_a():
    global Alarm
    Alarm = 0
    strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
input.on_button_pressed(Button.A, on_button_pressed_a)

Noise = 0
Alarm = 0
strip: neopixel.Strip = None
strip = neopixel.create(DigitalPin.P8, 1, NeoPixelMode.RGB)
Alarm = 0
strip.show_color(neopixel.colors(NeoPixelColors.RED))
basic.pause(1000)
strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
basic.pause(1000)
basic.show_icon(IconNames.YES)
basic.pause(1000)
basic.clear_screen()

def on_forever():
    if Alarm == 1:
        strip.show_color(neopixel.colors(NeoPixelColors.RED))
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
basic.forever(on_forever)

def on_forever2():
    global Noise
    Noise = smarthome.read_noise(AnalogPin.P2)
basic.forever(on_forever2)

def on_forever3():
    if Alarm == 0:
        basic.show_number(Noise)
    else:
        basic.show_icon(IconNames.NO)
basic.forever(on_forever3)

def on_forever4():
    global Alarm
    if Noise >= 100:
        Alarm = 1
basic.forever(on_forever4)
