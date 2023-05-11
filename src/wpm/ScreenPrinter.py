"""Handles printing text in the terminal window"""

from curses import color_pair

from typing import Tuple, Callable

from wpm.const import ColorPalette


class ScreenPrinter:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        ColorPalette(ColorPalette.NONE).init_palettes()

    def print_to_screen(self, pos: Tuple[int, int], text: str, palette_index: int):
        self.stdscr.clear()
        self.stdscr.addstr(*pos, text, color_pair(palette_index))
        self.stdscr.refresh()
