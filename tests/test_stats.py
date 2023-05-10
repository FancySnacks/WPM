import pytest

from wpm.StatTracker import StatTracker


@pytest.mark.parametrize('input, expected', [
    ((15, 3), 20),
    ((66, 12), 18),
])
def test_calculate_accuracy(input, expected):
    stats = StatTracker()
    stats.keystrokes, stats.successful_keystrokes = input

    assert stats.get_accuracy == expected
