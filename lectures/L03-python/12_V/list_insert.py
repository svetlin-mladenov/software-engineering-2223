def insert(array, number, index):
    return array[:index] + [number] + array[index:]

def test_insert():
    assert insert([1, 2, 3, 4], 5, 3) == [1, 2, 3, 5, 4]

array = [1, 2, 3, 4]