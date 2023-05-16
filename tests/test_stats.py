import pytest

import time

from wpm.StatTracker import StatTracker, Accuracy, WPM, Timer


@pytest.fixture
def stats() -> StatTracker:
    stats: StatTracker = StatTracker(stdscr=None, accuracy_tracker=Accuracy(), wpm_tracker=WPM(), timer=Timer())
    return stats


@pytest.mark.parametrize('input, expected', [
    ((15, 3), 20),
    ((66, 12), 18),
])
def test_calculate_accuracy(input: tuple[int, int], expected: int):
    stats = Accuracy()
    stats.keystrokes, stats.successful_keystrokes = input

    assert stats.get_accuracy == expected


@pytest.mark.parametrize('input, expected', [
    ((['a', 'p', 'p', 'l', 'e'], ['a', 'w', 'p', 'l', 'e']), 80),
])
def test_calculate_accuracy_from_list_of_words(input: list[str], expected: int):
    stats = Accuracy()
    stats.keystrokes = len(input[0])
    comparison = list(zip(input[0], input[1]))
    stats.successful_keystrokes = len([x for x in comparison if x[0] == x[1]])

    assert stats.get_accuracy == expected


@pytest.mark.parametrize("text, elapsed_time, expected", [
    ("bulletproof", 2, 66),
    ("iridescent", 1, 120),
    ("rozrewolwerowany rewolwerowiec z rozrewolwerowanym rewolwerem", 5, 146),
])
def test_wpm_calculation(text: str, elapsed_time: int, expected: int):
    stats = WPM()
    wpm: int = stats.get_wpm(text, elapsed_time)
    assert wpm == expected


@pytest.mark.parametrize("text, expected", [
    ("bulletproof", 132),
    ("iridescent", 120),
    ("rozrewolwerowany rewolwerowiec z rozrewolwerowanym rewolwerem", 732),
])
def test_StatTracker_wpm(stats: StatTracker, text: str, expected: int):
    wpm: int = stats.get_wpm(text)
    assert wpm == expected


@pytest.mark.parametrize("values, expected", [
    ((15, 3), 20),
    ((66, 12), 18),
])
def test_StatTracker_accuracy(stats: StatTracker, values: tuple[int, int], expected: int):
    stats.accuracy.keystrokes = values[0]
    stats.accuracy.successful_keystrokes = values[1]
    accuracy: int = stats.get_accuracy
    assert accuracy is expected
