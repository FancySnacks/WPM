from wpm.const import ESCAPE_KEY


def user_wants_to_exit(key: str | bytes) -> bool:
    if ord(key) == ESCAPE_KEY:
        return True
    else:
        return False


def is_backspace_key(key: str) -> bool:
    if key in ("KEY_BACKSPACE", '\b', '\x7f'):
        return True
    else:
        return False
