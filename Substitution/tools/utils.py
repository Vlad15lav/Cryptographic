import re

def check_regex(txt: str) -> bool:
    return len(re.sub(r'[А-Яа-яЁё ]', '', txt)) > 0