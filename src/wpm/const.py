import curses


ESCAPE_KEY = 27

# MESSAGES

WELCOME_MSG = "Welcome to the speed typing test!\n" \
              "Press Any key to begin..."

# PALETTES

COLOR_INFO = (curses.COLOR_GREEN, curses.COLOR_BLACK)
COLOR_SEQUENCE = (curses.COLOR_WHITE, curses.COLOR_BLACK)
COLOR_INPUT_CORRECT = (curses.COLOR_GREEN, curses.COLOR_BLACK)
COLOR_INPUT_INCORRECT = (curses.COLOR_RED, curses.COLOR_BLACK)
