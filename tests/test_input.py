import pytest

from wpm.util import user_wants_to_exit
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


def test_user_wants_to_exit():
    key_input = b'\x1b'
    is_escape_key = user_wants_to_exit(key_input)
    assert is_escape_key is True
