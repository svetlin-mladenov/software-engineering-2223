def compress(message):
    """Compress message using run length encoding

    :param message: string to encode
    """
    last = ""
    compressed = ""

    first = True
    consecutive_matches = 1
    for char in message:
        if first:
            last = char
            first = False
            compressed += char
        else:
            if char == last:
                consecutive_matches += 1
            else:
                compressed += str(consecutive_matches)
                compressed += char
                consecutive_matches = 1
            last = char
    compressed += str(consecutive_matches)
    if len(compressed) > len(message):
        return message
    return compressed


def test_compress():
    # pylint: disable=missing-function-docstring
    assert compress("aabcccccaaa") == "a2b1c5a3"
    assert compress("aabccccca") == "a2b1c5a1"


def test_inefficient_compression():
    # pylint: disable=missing-function-docstring
    assert compress("abc") == "abc"
