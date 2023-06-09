import curses
from curses import wrapper

from wpm.WordSequence import WordSequence
from wpm.UserInputController import UserInputController
from wpm.StatTracker import StatTracker, WPM, Accuracy, Timer
from wpm.const import ColorPalette


def main(stdscr=None):
    if not stdscr:
        stdscr = curses.initscr()

    curses.curs_set(0)

    ColorPalette.init_palettes()

    words = WordSequence.generate_sequence_from_file()

    user_controller = UserInputController(stdscr,
                                          words=words,
                                          stats=StatTracker(stdscr,
                                                            accuracy_tracker=Accuracy(),
                                                            timer=Timer(),
                                                            wpm_tracker=WPM()))
    user_controller.inspect_input()


if __name__ == "__main__":
    raise SystemExit(wrapper(main))
