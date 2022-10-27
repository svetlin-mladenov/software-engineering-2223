import string


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
      
    if(len(new_list) > len(message)):
        return message
    else:
        return new_list

def test_str_compress():
    assert compress("aabcccccaaa") == "a2b1c5a3"
    assert compress("aabccccca") == "a2b1c5a1"
    assert compress("abc") == "abc"
    assert compress("a") == "a"