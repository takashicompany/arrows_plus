print("Arrows+ Starting")

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner
from kmk.modules.layers import Layers
from kmk.handlers.sequences import send_string

_KEY_CFG = [
    board.D9,
    board.D10,
    board.D3,
    board.D2,
    board.D8
]

layers = Layers()

# Keyboard implementation class
class ArrowsPlus(KMKKeyboard):
    def __init__(self):
        # create and register the scanner
        self.matrix = KeysScanner(
            # require argument:
            pins=_KEY_CFG,
            # optional arguments with defaults:
            value_when_pressed=False,
            pull=True,
            interval=0.02,  # Debounce time in floating point seconds
            max_events=64
        )

keyboard = ArrowsPlus()
keyboard.modules = [layers]

keyboard.keymap = [
    [
        KC.W, KC.E,
        KC.A, KC.S, KC.D
    ],
]

if __name__ == '__main__':
    keyboard.go()