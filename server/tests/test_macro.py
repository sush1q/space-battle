from server.interfaces import *
from server.macro_commands import *


def test_macro():
    obj = UObject(
        {
            'position': Point(12, 5),
            'velocity': Point(-7, 3),
            'fuel_amount': 10,
            'fuel_burn_rate': 5
        }
    )
    moveable_obj = MoveAndBurnFuelAdapter(obj)
    move = MoveAndBurnFuel(moveable_obj)
    move()
    assert moveable_obj.get_position() == (5, 8) and moveable_obj.get_fuel_amount() == 5

def test_macro_no_fuel():
    obj = UObject(
        {
            'position': Point(12, 5),
            'velocity': Point(-7, 3),
            'fuel_amount': 2,
            'fuel_burn_rate': 5
        }
    )
    moveable_obj = MoveAndBurnFuelAdapter(obj)
    move = MoveAndBurnFuel(moveable_obj)
    try:
        move()
    except CommandException:
        assert True
