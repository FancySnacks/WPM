import pytest

from wpm.util import user_wants_to_exit, is_backspace_key
from wpm.UserInputController import UserInputController


@pytest.mark.parametrize("value, index, expected", [
    ("hello", 0, "h"),
    ("dungeon", 3, "g"),
    ("sky limit", 4, "l"),
])
def test_is_input_char_valid(value, index, expected):
    sequence: str = value
    input_controller = UserInputController(None, sequence, None)
    char_input = input_controller.is_char_correct(expected, index)
    assert char_input is True


@pytest.mark.parametrize("value, expected", [
    (b'\x1b', True),
    (27, True),
    ('esc', False)
])
def test_is_escape_key(value: str | bytes, expected: bool):
    is_escape_key = user_wants_to_exit(value)
    assert is_escape_key is expected


@pytest.mark.parametrize("value, expected", [
    ('\x7f', True),
    ('\b', True),
    ('KEY_BACKSPACE', True),
    ('esc', False),
    ('t', False),
])
def test_is_backspace_key(value: str, expected: bool):
    is_backspace = is_backspace_key(value)
    assert is_backspace is expected
