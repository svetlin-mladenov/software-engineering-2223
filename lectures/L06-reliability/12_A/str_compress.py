import pytest


def compress(message):
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

    if (len(new_list) > len(message)):
        return message
    else:
        return new_list


@pytest.mark.parametrize("input, output", [
    ("aabcccccaaa", "a2b1c5a3"),
    ("aabccccca", "a2b1c5a1"),
    ("abc", "abc"),
    ("a", "a"),
    ("Caseeee", "Caseeee")
])
def test_str_compress(input, output):
    assert compress(input) == output
