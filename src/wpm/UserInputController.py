import curses

from wpm.WordSequence import WordSequence
from wpm.util import is_backspace_key, user_wants_to_exit


class UserInputController:
    def __init__(self, stdscr: curses.window, words: WordSequence):
        self.stdscr = stdscr

        self.words = words
        self.current_text: list[str] = []

        self.active: bool = True

    def inspect_input(self):
        while self.active:
            self.refresh()

            key = self.stdscr.getkey()

            if user_wants_to_exit(key):
                return 1
            elif is_backspace_key(key):
                if len(self.current_text) > 0:
                    self.remove_char()
            else:
                self.current_text.append(key)

    def is_char_correct(self, key: str, index: int) -> bool:
        if key in self.words.sequence[index]:
            return True
        else:
            return False

    def print_text(self):
        self.stdscr.addstr(self.words.sequence, 3)

        for i, char in enumerate(self.current_text):
            color = 3 if self.is_char_correct(char, i) else 4
            self.stdscr.addstr(0, i, char, curses.color_pair(color))

    def refresh(self):
        self.stdscr.clear()
        self.print_text()
        self.stdscr.refresh()

    def remove_char(self):
        self.current_text.pop()