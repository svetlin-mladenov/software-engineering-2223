import pytest

def insert(array, pos, object):
    if pos < 0:
        pos = len(array) + pos
    d = 0
    result = []

    for elemnt in array:
        if  d == pos:
            result.append(object) 
            
        result.append(elemnt)     
        d += 1
    if  d == pos:
        result.append(object) 
            
    return result
    

def test_list_insert():
    assert insert(["a", "b"], 2, "c") == ["a", "b", "c"]
    assert insert(["a", "b"], 1, "c") == ["a", "c", "b"]
    assert insert(["a", "b"], 0, "c") == ["c", "a", "b"]

def test_list_insert_negative_index():
    assert insert(["a", "b"], -1, "c") == ["a", "c", "b"]

# def test_index_oob():
#     with pytest.raises(IndexError):
#         insert(["a", "b"], 3, "c")