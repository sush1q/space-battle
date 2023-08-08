from ... import *
from types import MappingProxyType


def test_spin():
    obj = UObject(
        {
            'direction': 2,
            'directions_number': 8,
            'angular_velocity': 1
        }
    )
    spinable_obj = SpinableAdapter(obj)
    spin = Spin(spinable_obj)
    spin()
    assert spinable_obj.get_direction() == 3

def test_spin_no_direction():
    obj = UObject(
        {
            'directions_number': 8,
            'angular_velocity': 1
        }
    )
    spinable_obj = SpinableAdapter(obj)
    spin = Spin(spinable_obj)
    try:
        spin()
    except KeyError:
        assert True

def test_spin_no_directions_number():
    obj = UObject(
        {
            'direction': 8,
            'angular_velocity': 1
        }
    )
    spinable_obj = SpinableAdapter(obj)
    spin = Spin(spinable_obj)
    try:
        spin()
    except KeyError:
        assert True

def test_spin_no_angular_velocity():
    obj = UObject(
        {
            'direction': 2,
            'directions_number': 8,
        }
    )
    spinable_obj = SpinableAdapter(obj)
    spin = Spin(spinable_obj)
    try:
        spin()
    except KeyError:
        assert True

def test_spin_immutable_object():
    obj = UObject(
        MappingProxyType(
            {
                'directions_number': 8,
                'direction': 1,
                'angular_velocity': 1
            }
        )
    )
    spinable_obj = SpinableAdapter(obj)
    spin = Spin(spinable_obj)
    try:
        spin()
    except TypeError:
        assert True
