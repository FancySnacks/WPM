from dataclasses import dataclass


@dataclass
class StatTracker:
    keystrokes = 0
    successful_keystrokes = 0

    @property
    def get_accuracy(self) -> int:
        return int((self.successful_keystrokes / self.keystrokes) * 100)
