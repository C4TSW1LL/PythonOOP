import pytest
from src.Triangle import Triangle
from src.Rectangle import Rectangle
from src.Figure import Figure


def test_create_correct_triangle():
        Triangle(12, 13, 14)

def test_create_incorrect_triangle():
    with pytest.raises(ValueError):
        Triangle(1, 100, 1)

def test_check_area():
    triange = Triangle(12,13,14)
    assert 72 == triange.area()

def test_check_perimeter():
    triangle = Triangle(12,13,14)
    assert 39 == triangle.perimeter()

def test_add_area():
    triangle = Triangle(12,13,14)
    rectangle = Rectangle(10, 12)
    assert Figure.add_area(triangle, rectangle) == 100