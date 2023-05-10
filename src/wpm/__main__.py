import curses
from curses import wrapper

from wpm.WordSequence import WordSequence
from wpm.UserInputController import UserInputController
from wpm.StatTracker import StatTracker

from const import COLOR_INFO, COLOR_SEQUENCE, COLOR_INPUT_CORRECT, COLOR_INPUT_INCORRECT


def main(stdscr):
    curses.init_pair(1, *COLOR_INFO)
    curses.init_pair(2, *COLOR_SEQUENCE)
    curses.init_pair(3, *COLOR_INPUT_CORRECT)
    curses.init_pair(4, *COLOR_INPUT_INCORRECT)

    words = WordSequence()
    words.generate_sequence(6)

    user_controller = UserInputController(stdscr, words=words, stats=StatTracker())
    user_controller.inspect_input()


if __name__ == "__main__":
    raise SystemExit(wrapper(main))
