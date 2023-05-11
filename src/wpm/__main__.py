from curses import wrapper

from wpm.WordSequence import WordSequence
from wpm.UserInputController import UserInputController
from wpm.StatTracker import StatTracker, WPM, Accuracy
from wpm.const import ColorPalette


def main(stdscr):
    ColorPalette.init_palettes()

    words = WordSequence()
    words.generate_sequence(6)

    user_controller = UserInputController(stdscr,
                                          words=words,
                                          stats=StatTracker(stdscr,
                                                            accuracy_tracker=Accuracy(),
                                                            wpm_tracker=WPM()))
    user_controller.inspect_input()


if __name__ == "__main__":
    raise SystemExit(wrapper(main))
