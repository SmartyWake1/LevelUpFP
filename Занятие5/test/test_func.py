import pytest as pytest

from Занятие5.test.func import division


def test_division():
    a, b = 3, 3
    result = division(a, b)
    assert result == 1

def test_division_zero():
    a, b = 3, 0
    result = division(a, b)
    assert result == 1


def test_division_zero_error():
    a, b = 3, 0
    with pytest.raises(ValueError):
        division(a, b)
