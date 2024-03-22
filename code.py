import time
import digitalio
import board
import usb_hid
import neopixel
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

boton1_pin= board.GP15
boton2_pin= board.GP14
boton3_pin= board.GP13

teclado = Keyboard(usb_hid.devices)

boton1 = digitalio.DigitalInOut(boton1_pin)
boton1.direction = digitalio.Direction.INPUT
boton1.pull = digitalio.Pull.DOWN

boton2 = digitalio.DigitalInOut(boton2_pin)
boton2.direction = digitalio.Direction.INPUT
boton2.pull = digitalio.Pull.DOWN

boton3 = digitalio.DigitalInOut(boton3_pin)
boton3.direction = digitalio.Direction.INPUT
boton3.pull = digitalio.Pull.DOWN

led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 0.3
led[0] = (0, 255, 0)

while True:
    if boton1.value:
        led[0] = (255, 0, 0)
        print("Botón 1 - Canción anterior")
        teclado.press(Keycode.CONTROL, Keycode.LEFT_ARROW)
        time.sleep(0.5)
        teclado.release(Keycode.CONTROL, Keycode.LEFT_ARROW)
        led[0] = (0, 255, 0)
    if boton2.value:
        led[0] = (255, 0, 0)
        print("Botón 2 - Pausar canción")
        teclado.press(Keycode.CONTROL, Keycode.SPACE)
        time.sleep(0.5)
        teclado.release(Keycode.CONTROL, Keycode.SPACE)
        led[0] = (0, 255, 0)
    if boton3.value:
        led[0] = (255, 0, 0)
        print("Botón 3 - Canción siguiente")
        teclado.press(Keycode.CONTROL, Keycode.RIGHT_ARROW)
        time.sleep(0.5)
        teclado.release(Keycode.CONTROL, Keycode.RIGHT_ARROW)
        led[0] = (0, 255, 0)

    