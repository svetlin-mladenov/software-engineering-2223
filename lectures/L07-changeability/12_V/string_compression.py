def complicated_func(param1, param2, param3):
    """aksdljflkadf"""
    if param1 > param2:
        param3 += param1
    if param2 > param3:
        param1 = param3 - param2
    if param2 > param3:
        param1 = param3 - param2
    if param2 > param3:
        param1 = param3 - param2
    if param2 > param3:
        param1 = param3 - param2
    if param2 > param3:
        param1 = param3 - param2
    if param2 > param3:
        param1 = param3 - param2
    if param2 > param3:
        param1 = param3 - param2
    if param2 > param3:
        param1 = param3 - param2
    if param2 > param3:
        param1 = param3 - param2
    return param1


def compress(message):
    """Compress message using run length coding.

    :param message: string to compress
    """
    compressed = ""

    i = 0
    while i < len(message):
        j = i+1
        count = 1
        while j < len(message):
            if message[j] == message[i]:
                count += 1
            else:
                break
            j += 1
        compressed += message[i] + str(count)
        i = j

    if len(message) < len(compressed):
        return message
    return compressed


def test_compression():
    # pylint: disable=missing-function-docstring
    assert compress("") == ""
    assert compress("aabcccccaaa") == "a2b1c5a3"
    assert compress("aaaaaaab") == "a7b1"


def test_bad_compression():
    # pylint: disable=missing-function-docstring
    assert compress("aloda") == "aloda"
