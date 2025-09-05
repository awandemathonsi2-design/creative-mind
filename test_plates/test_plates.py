import pytest
from plates import is_valid

def main():
    test_first_alpha()
    test_length()
    test_place_digits()
    test_alnum()

#Tests that the first characters are letters
def test_first_alpha():
    assert is_valid("HE110") == True
    assert is_valid("11HELP") == False
    assert is_valid("5C") == False
    assert is_valid("C5") == False

#Tests that the max length is six and min length is two
def test_length():
    assert is_valid("AB") == True
    assert is_valid("NRVOUS") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False

#Tests that the first digit is not 0 and that the digits are at the end
def test_place_digits():
    assert is_valid("AAA022") == False
    assert is_valid("AAA22A") == False
    assert is_valid("AAAA20") == True

#Tests that there are no punctuation marks
def test_alnum():
    assert is_valid("ABCD.") == False
    assert is_valid("HE!!O") == False

if __name__ == "__main__":
    main()