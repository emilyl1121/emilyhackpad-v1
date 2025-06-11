# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here!
PINS = [board.GP1, board.GP2, board.GP3, board.GP4]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# define the buttons corresponding to the pins
keyboard.keymap = [
    [KC.Macro(Press(KC.LCTRL), Tap(KC.C), Release(KC.LCTRL)), KC.Macro(Press(KC.LCTRL), Tap(KC.V), Release(KC.LCTRL)), KC.F6, KC.F11]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()