"""Examines user's input"""

from __future__ import annotations

import curses

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from wpm.WordSequence import WordSequence
    from wpm.StatTracker import StatTracker

from wpm.util import is_backspace_key, user_wants_to_exit


class UserInputController:
    def __init__(self, stdscr: curses.window, words: WordSequence, stats: StatTracker):
        self.stdscr = stdscr
        self.stat_tracker = stats
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
                correct = self.is_char_correct(key, len(self.current_text)-1)
                self.increment_key_stats(correct)

    def is_char_correct(self, key: str, index: int) -> bool:
        if key == self.words.sequence[index]:
            return True
        else:
            return False

    def print_text(self):
        self.stdscr.addstr(self.words.sequence, 3)

        for i, char in enumerate(self.current_text):
            correct = self.is_char_correct(char, i)
            color = 3 if correct else 4
            self.stdscr.addstr(0, i, char, curses.color_pair(color))

        self.print_accuracy()

    def print_accuracy(self):
        self.stdscr.addstr(1, 0, f'ACC: {self.stat_tracker.get_accuracy}%', curses.color_pair(1))

    def refresh(self):
        self.stdscr.clear()
        self.print_text()
        self.stdscr.refresh()

    def remove_char(self):
        self.current_text.pop()

    def increment_key_stats(self, correct):
        self.stat_tracker.increment_stat('keystrokes', 1)

        if correct:
            self.stat_tracker.increment_stat('successful_keystrokes', 1)
