from typing import Annotated, Final, Literal


def clamp(val, min_val, max_val):
    return max(min_val, min(max_val, val))

def strcmp(s1: str, s2: str) -> Literal[-1, 0, 1]:
    len_diff: Final = len(s1) - len(s2)
    if len_diff:
        return clamp(len_diff, -1, 1)
    len_diff = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return clamp(ord(s1[i]) - ord(s2[i]), -1, 1)
    return 0


def test_strcmp():
    assert strcmp("abc", "abc") == 0
    assert strcmp("Abc", "abc") == -1
    assert strcmp("abc", "Abc") == 1


def my_fun() -> Annotated[int, ValueRange[-1, 1]]:
    pass
