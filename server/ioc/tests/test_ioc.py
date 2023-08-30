from server import *


def test_ioc_resolve_existing_object():
    obj = IoC.resolve(
        'UObject', 
        {
            'fuel_amount': 10,
            'fuel_burn_rate': 5
        }
    )
    assert type(obj) == UObject

def test_ioc_resolve_unexisting_object():
    try:
        IoC.resolve(
            'ThisObjectIsNeverUsed', 
            {
                'fuel_amount': 10
            }
        )
    except:
        assert True

def test_ioc_register_lambda():
    obj = IoC.resolve(
        'IoC.register',
        'NewObject',
        lambda x: x*x
    )
    assert type(obj).__name__ == 'NewObject'
