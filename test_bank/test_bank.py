import pytest
from bank import value

def main():
    test_bank()
    test_h()
    test_anything()

#Tests that 0 is returned
def test_bank():
    assert value("hello") == 0
    assert value(" hello ") == 0
    assert value("HELLO") == 0

#Tests that 20 is returned
def test_h():
    assert value("hey") == 20
    assert value("HOWDY") == 20

#Tests that 100 is returned
def test_anything():
    assert value("whazzup") == 100

if __name__ == "__main__":
    main()