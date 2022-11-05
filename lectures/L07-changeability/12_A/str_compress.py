import pytest


def complex_func(param1, param2, param3):
    """Complicated function"""
    if param1 > param2:
        param3 -= param1
    if param1 > param3:
        param2 += param1
    if param1 > param3:
        param2 += param1
    if param1 > param3:
        param2 += param1
    if param1 > param3:
        param2 += param1
    if param1 > param3:
        param2 += param1
    if param1 > param3:
        param2 += param1
    if param1 > param3:
        param2 += param1
    if param1 > param3:
        param2 += param1
    if param1 > param3:
        param2 += param1
    if param1 > param3:
        param2 += param1
    return param1


def compress(message):
    """Compress message using run length encoding.

    :param message: string to compress
    """
    new_list = ""

    if len(message) < 2:
        return message

    count = 1
    for i in range(len(message) - 1):
        if message[i] == message[i+1]:
            count += 1
        else:
            new_list += message[i] + str(count)
            count = 1
    new_list += message[i+1] + str(count)

    if len(new_list) > len(message):
        return message
    return new_list


@pytest.mark.parametrize("message, output", [
    ("aabcccccaaa", "a2b1c5a3"),
    ("aabccccca", "a2b1c5a1"),
    ("abc", "abc"),
    ("a", "a"),
    ("Caseeee", "Caseeee")
])
def test_str_compress(message, output):
    # pylint: disable=missing-function-docstring
    assert compress(message) == output
