from palindrome import *

def test_palindrome():
    assert is_palindrome("racecar")
    assert is_palindrome("")
    assert is_palindrome("a")
    assert is_palindrome("123321")
    assert not is_palindrome("abc")