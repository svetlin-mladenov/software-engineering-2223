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