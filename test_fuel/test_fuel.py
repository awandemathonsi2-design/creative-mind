import pytest
from fuel import convert, gauge

def main():
    test_convert()
    test_convert_zero_division_error()
    test_convert_value_error()
    test_gauge()

#Tests correct conversion
def test_convert():
    assert convert("1/3") == 33
    assert convert("2/4") == 50

#Tests ZeroDivisionError
def test_convert_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        assert convert("3/0")

#Tests ValueError
def test_convert_value_error():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        assert convert("3/2")
    with pytest.raises(ValueError):
        assert convert("-1/4")

#Tests gauge
def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"

if __name__ == "__main__":
    pytest.main()