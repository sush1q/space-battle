from ... import *


def test_point():
    assert Point(5, 10) == (5, 10)

def test_point_add():
    a = Point(5, 10)
    b = Point(2, 1)
    assert a+b == (7,11)

def test_point_sub():
    a = Point(5, 10)
    b = Point(2, 1)
    assert a-b == (3,9)
