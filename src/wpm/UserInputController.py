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
        self._current_text: list[str] = []

        self.active: bool = True

    @property
    def current_text(self) -> str:
        return ' '.join(self._current_text)

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
                self._current_text.append(key)
                correct = self.is_char_correct(key, len(self._current_text)-1)
                self.increment_key_stats(correct)

    def is_char_correct(self, key: str, index: int) -> bool:
        if key == self.words.sequence[index]:
            return True
        else:
            return False

    def print_text(self):
        self.stdscr.addstr(0, 0, self.words.sequence, curses.color_pair(2))

        for i, char in enumerate(self._current_text):
            correct = self.is_char_correct(char, i)
            color = 3 if correct else 4
            self.stdscr.addstr(0, i, char, curses.color_pair(color))

        self.stat_tracker.print_accuracy()
        self.stat_tracker.print_wpm(self.current_text)

    def refresh(self):
        self.stdscr.clear()
        self.print_text()
        self.stdscr.refresh()

    def remove_char(self):
        self._current_text.pop()

    def increment_key_stats(self, correct):
        self.stat_tracker.accuracy.increment_stat('keystrokes', 1)

        if correct:
            self.stat_tracker.accuracy.increment_stat('successful_keystrokes', 1)
