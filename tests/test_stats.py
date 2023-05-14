import pytest

import time

from wpm.StatTracker import Accuracy, WPM


@pytest.mark.parametrize('input, expected', [
    ((15, 3), 20),
    ((66, 12), 18),
])
def test_calculate_accuracy(input, expected):
    stats = Accuracy()
    stats.keystrokes, stats.successful_keystrokes = input

    assert stats.get_accuracy == expected


@pytest.mark.parametrize('input, expected', [
    ((['a', 'p', 'p', 'l', 'e'], ['a', 'w', 'p', 'l', 'e']), 80),
])
def test_calculate_accuracy_from_list_of_words(input, expected):
    stats = Accuracy()
    stats.keystrokes = len(input[0])
    comparison = list(zip(input[0], input[1]))
    stats.successful_keystrokes = len([x for x in comparison if x[0] == x[1]])

    assert stats.get_accuracy == expected


@pytest.mark.skip(reason="TODO")
def test_wpm_calculation(input, expected):
    #TODO
    assert 1 == 0
