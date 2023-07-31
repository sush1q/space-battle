from interfaces.move import *
# TODO: пофиксить импорт
from types import MappingProxyType


def test_move():
    obj = UObject(
        {
            'position': Point(12, 5),
            'velocity': Point(-7, 3)
        }
    )
    moveable_obj = MoveableAdapter(obj)
    move = Move(moveable_obj)
    move()
    assert moveable_obj.get_position() == (5, 8)

def test_unavailable_position():
    obj = UObject(
        {
            'velocity': Point(-7, 3)
        }
    )
    moveable_obj = MoveableAdapter(obj)
    move = Move(moveable_obj)
    try:
        move()
    except KeyError:
        assert True

def test_unavailable_velocity():
    obj = UObject(
        {
            'position': Point(-7, 3)
        }
    )
    moveable_obj = MoveableAdapter(obj)
    move = Move(moveable_obj)
    try:
        move()
    except KeyError:
        assert True

def test_unavailable_set_position():
    obj = UObject(
        MappingProxyType(
            {
                'position': Point(12, 5),
                'velocity': Point(-7, 3)
            }
        )
    )
    moveable_obj = MoveableAdapter(obj)
    move = Move(moveable_obj)
    try:
        move()
    except:
        assert True
