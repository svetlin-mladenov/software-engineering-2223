def my_insert(seq, index, elem):
    new_seq = []
    if index < 0 and :
        index = len(seq) +  index + 1

    for i in range(len(seq) + 1):
        if i == index:
            new_seq.append(elem)
        elif i <= index:
            new_seq.append(seq[i])
        else:
            new_seq.append(seq[i - 1])

    return new_seq