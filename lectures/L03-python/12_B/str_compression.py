from copyreg import constructor
from os import truncate

from pkg_resources import resource_string


def compress(message):
    last = ""
    compressed = ""
    first = True
    consecutive_matches = 1
    for c in message:
        if first:
            last = c
            first = False
            compressed += c
        else:
            if c == last:
                consecutive_matches += 1
            else:
                compressed += str(consecutive_matches)
                compressed += c
                consecutive_matches = 1
            last = c
    compressed += str(consecutive_matches)
    return compressed


def test_compress():
    assert compress("aabcccccaaa") == "a2b1c5a3"
    assert compress("aabccccca") == "a2b1c5a1"

def 
    assert compress("") == ""

test_compress()