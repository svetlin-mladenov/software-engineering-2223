import pytest


def copy(destParam, sourceParam, x, y):
    dest = destParam
    source = sourceParam

    if(not (0 <= x < len(dest[0]))) or (not (0 <= y < len(dest))):
        raise IndexError()

    for i in range(len(source)):
        for j in range(len(source[0])):
            dest[i + y][j + x] = source[i][j]
    return dest

def test_copy():
    assert copy(
        [
            [1, 2, 3, 4],
            [1, 2, 3, 4]
        ], [
            [5, 6],
            [7, 8]
        ], 0, 0) == [
            [5, 6, 3, 4],
            [7, 8, 3, 4]
        ]

    with pytest.raises(IndexError):
        copy([[]], [[]], 1, 1)

    with pytest.raises(IndexError):
        copy(
        [
            []
        ], [
            []
        ], 0, 0) == [[]]
    
    with pytest.raises(IndexError):
        assert copy(
            [
                [2, 3],
                [4, 5]
            ],
            [
                [1, 6, 7],
                [8,9,10]
            ], 0, 0
        )