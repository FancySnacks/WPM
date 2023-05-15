"""Tracks user stats like accuracy and WPM"""

from __future__ import annotations

from time import time, strftime
from dataclasses import dataclass


class StatTracker:

    palette = 1

    def __init__(self, stdscr, accuracy_tracker: Accuracy, timer: Timer, wpm_tracker: WPM):
        self.stdscr = stdscr
        self.accuracy = accuracy_tracker
        self.timer = timer
        self.wpm = wpm_tracker

        self.timer.start_timer()

    def get_wpm(self, text: str) -> int:
        return self.wpm.get_wpm(text, self.get_time_elapsed)

    @property
    def get_accuracy(self) -> int:
        return self.accuracy.get_accuracy

    @property
    def get_time_elapsed(self) -> int:
        return int(self.timer.elapsed_time)

    def print_wpm(self, text: str):
        self.stdscr.addstr(1, 0, f'WPM: {self.get_wpm(text)}', self.palette)

    def print_accuracy(self):
        self.stdscr.addstr(1, 10, f'ACC: {self.get_accuracy}%', self.palette)

    def print_elapsed_time(self):
        if self.get_time_elapsed >= 60:
            formatted_time: str = f'{(self.get_time_elapsed / 60):02d}:{(self.get_time_elapsed % 60):02d}'
        else:
            formatted_time: str = f'00:{self.get_time_elapsed:02d}'

        self.stdscr.addstr(1, 20, f'{formatted_time}', self.palette)


@dataclass
class Accuracy:
    keystrokes = 0
    successful_keystrokes = 0

    @property
    def get_accuracy(self) -> int:
        try:
            return int((self.successful_keystrokes / self.keystrokes) * 100)
        except ZeroDivisionError:
            return 0

    def increment_stat(self, name: str, value):
        current_value = getattr(self, name)
        setattr(self, name, current_value + value)


class Timer:
    def __init__(self):
        self.start_time = None

    def start_timer(self):
        self.start_time = time()

    @property
    def elapsed_time(self) -> float:
        return max(time() - self.start_time, 1)


class WPM:
    @staticmethod
    def get_wpm(text: str, elapsed_time: int) -> int:
        wpm = len(text) / (elapsed_time / 60) / 5
        return int(wpm)
