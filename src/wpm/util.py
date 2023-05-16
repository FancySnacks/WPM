from wpm.const import ESCAPE_KEY


def user_wants_to_exit(key: str | bytes | int) -> bool:
    if key in (b'\x1b', ESCAPE_KEY):
        return True
    elif len(key) == 1 and ord(key) == ESCAPE_KEY:
        return True
    else:
        return False


def is_backspace_key(key: str) -> bool:
    match key:
        case "KEY_BACKSPACE": return True
        case '\b': return True
        case '\x7f': return True
        case _: return False
