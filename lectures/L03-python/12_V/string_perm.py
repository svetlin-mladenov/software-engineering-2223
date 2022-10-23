def is_perm_eq(str1, str2):
    return sorted(str1) == sorted(str2) 

        


def test_string_perm_eq():
    assert is_perm_eq("abc", "cba")
    assert is_perm_eq("abc", "abc")
    assert not is_perm_eq("abc", "abcd")
    assert not is_perm_eq("abc", "ab")
    assert is_perm_eq("", "")