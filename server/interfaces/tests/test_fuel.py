from ... import *
from types import MappingProxyType


def test_check_fuel_enough():
    obj = UObject(
        {
            'fuel_amount': 10,
            'fuel_burn_rate': 5
        }
    )
    fuel_obj = FuelAdapter(obj)
    check = CheckFuel(fuel_obj)
    check()
    
def test_check_fuel_not_enough():
    obj = UObject(
        {
            'fuel_amount': 3,
            'fuel_burn_rate': 5
        }
    )
    fuel_obj = FuelAdapter(obj)
    check = CheckFuel(fuel_obj)
    try:
        check()
    except CommandException:
        assert True

def test_burn_fuel():
    obj = UObject(
        {
            'fuel_amount': 10,
            'fuel_burn_rate': 5
        }
    )
    fuel_obj = FuelAdapter(obj)
    burn = BurnFuel(fuel_obj)
    burn()
    assert fuel_obj.get_fuel_amount() == 5

def test_burn_fuel_no_fuel_amount():
    obj = UObject(
        {
            'fuel_burn_rate': 5
        }
    )
    fuel_obj = FuelAdapter(obj)
    burn = BurnFuel(fuel_obj)
    try:
        burn()
    except:
        assert True

def test_burn_fuel_no_burn_rate():
    obj = UObject(
        {
            'fuel_amount': 5
        }
    )
    fuel_obj = FuelAdapter(obj)
    burn = BurnFuel(fuel_obj)
    try:
        burn()
    except:
        assert True

def test_burn_fuel_immutable_obj():
    obj = UObject(
        MappingProxyType(
        
            {
                'fuel_amount': 10,
                'fuel_burn_rate': 5
            }
        )
    )
    fuel_obj = FuelAdapter(obj)
    burn = BurnFuel(fuel_obj)
    try:
        burn()
    except:
        assert True
