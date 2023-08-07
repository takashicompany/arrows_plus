print("Arrows Plus Starting")

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner
from kmk.modules.layers import Layers
from kmk.handlers.sequences import send_string
from kmk.modules.encoder import EncoderHandler

_KEY_CFG = [
    board.A3,
    board.D10,
    board.A0,
    board.A1,
    board.A2
]

encoder_handler = EncoderHandler()
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
keyboard.modules = [layers, encoder_handler]

MyKey = send_string("This is Arrows Plus.")

keyboard.keymap = [
    [
        KC.W, KC.E,
        KC.A, KC.S, KC.D
    ],
]

encoder_handler.pins = ((board.D9, board.D8),)

encoder_handler.map =   [
                            ((KC.A, KC.Z),)
                        ]

if __name__ == '__main__':
    keyboard.go()