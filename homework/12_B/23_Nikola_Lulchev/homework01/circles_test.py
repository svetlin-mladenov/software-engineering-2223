from circles import check

def test_check():
    assert check(1, 1, 1, 2, 2, 3) == 3
    assert check(1, 1, 1, 1, 1, 1) == 1
