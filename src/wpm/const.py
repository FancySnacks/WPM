import curses

import pathlib


class ColorPalette:
    colors = [
    (curses.COLOR_GREEN, curses.COLOR_RED),
    (curses.COLOR_WHITE, curses.COLOR_BLACK),
    (curses.COLOR_GREEN, curses.COLOR_BLACK),
    (curses.COLOR_RED, curses.COLOR_BLACK)
    ]

    @classmethod
    def init_palettes(cls):
        curses.start_color()

        for index, palette in enumerate(cls.colors):
            # NOTE: The index can't be 0 or less, it will throw an exception
            curses.init_pair(index+1, *palette)



ESCAPE_KEY = 27

WELCOME_MSG = "Welcome to the speed typing test!\n" \
              "Press Any key to begin..."

PATH = pathlib.Path(__file__).parent
DEFAULT_WORDLIST_PATH = PATH.joinpath('words.txt')
