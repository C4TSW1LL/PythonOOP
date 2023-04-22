import pytest

from src.Rectangle import Rectangle


def test_create_rectangle():
    assert Rectangle(10, 13)

def test_create_incorrect_rectangle():
    with pytest.raises(ValueError):
        Rectangle(0, 12)

def test_check_area():
    rectangle = Rectangle(10,13)
    assert rectangle.area() == 130