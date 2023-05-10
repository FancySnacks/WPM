from dataclasses import dataclass


@dataclass
class StatTracker:
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
