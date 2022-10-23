def is_perm(str1, str2):
    return sorted(str1) == sorted(str2)

def test_str_perm():
    assert is_perm("abc", "cba")
    assert is_perm("", "")
    assert is_perm("abc", "abc")
    assert not is_perm("abc", "adb")