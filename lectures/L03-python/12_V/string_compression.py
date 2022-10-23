from email import message


def compress(message):
    compressed = ""

    i = 0
    while i < len(message):
        c = message[i]
        j = i+1
        count = 1
        while j < len(message):
            if message[j] == message[i]:
                count+=1
            else:
                break
            j+=1
        compressed += message[i] + str(count)
        if len(message) < len(compressed):
            return message
        i=j

    return compressed


def test_compression():
    assert compress("") == ""
    assert compress("aabcccccaaa") == "a2b1c5a3"
    assert compress("aaaaaaab") == "a7b1"


def test_bad_compression():
    assert compress("aloda") == "aloda"