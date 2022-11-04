from main import find_relative_position

def test_find_relative_position():
    assert find_relative_position(1, 1, 2, 6, 1, 3) == 0
    assert find_relative_position(1, 1, 2, 6, 1, 1) == 1
    assert find_relative_position(1, 1, 2, 1.2, 1, 1.8) == 2
    assert find_relative_position(2, 2, 4, 1, 1, 1) == 3
    assert find_relative_position(1, 1, 2, 1, 2, 2) == 4
    