from insert import *
import pytest

def test_list_insert():
    assert my_insert([], 0, "a") == ["a"]
    assert my_insert(["b", "c"], 0, "a") == ["a", "b", "c"]
    assert my_insert(["b", "c"], 1, "a") == ["b", "a", "c"]
    assert my_insert(["b", "c"], 2, "a") == ["b", "c", "a"]

def test_my_insert_index_out_of_bounds():
    with pytest.raises(IndexError):
        my_insert(["b", "c"], 10, "a")
    with pytest.raises(IndexError):
        my_insert(["b", "c"], -10, "a")

def test_negative_indices():
    my_insert(["b", "c"], -1, "a") == ["b", "c", "a"]