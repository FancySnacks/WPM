import curses


class ColorPalette:
    colors = [
    (curses.COLOR_GREEN, curses.COLOR_BLACK),
    (curses.COLOR_WHITE, curses.COLOR_BLACK),
    (curses.COLOR_GREEN, curses.COLOR_BLACK),
    (curses.COLOR_RED, curses.COLOR_BLACK)
    ]

    @classmethod
    def init_palettes(cls):
        for index, palette in enumerate(cls.colors):
            curses.init_pair(index + 1, *palette)


ESCAPE_KEY = 27

# MESSAGES

WELCOME_MSG = "Welcome to the speed typing test!\n" \
              "Press Any key to begin..."
