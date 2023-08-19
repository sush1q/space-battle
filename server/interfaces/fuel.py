from .common import *


class CommandException(Exception):
    pass


class IFuel(ABC):
    @abstractmethod
    def get_fuel_amount(self, *args):
        pass
    
    @abstractmethod
    def get_fuel_burn_rate(self, *args):
        pass

    @abstractmethod
    def set_fuel_amount(self, *args):
        pass

class FuelAdapter(IFuel):
    fuel_property = 'fuel_amount'
    fuel_burn_rate = 'fuel_burn_rate'

    def __init__(self, obj: UObject) -> None:
        self.obj = obj

    def get_fuel_amount(self):
        return self.obj.get_property(FuelAdapter.fuel_property)
    
    def get_fuel_burn_rate(self):
        return self.obj.get_property(FuelAdapter.fuel_burn_rate)

    def set_fuel_amount(self, fuel_amount):
        return self.obj.set_property(FuelAdapter.fuel_property, fuel_amount)

class CheckFuel(ICommand):
    def __init__(self, obj:IFuel):
        self.obj = obj
        
    def __call__(self):
        amount = self.obj.get_fuel_amount()
        burn_rate = self.obj.get_fuel_burn_rate()
        if burn_rate > amount:
            raise CommandException

class BurnFuel(ICommand):
    def __init__(self, obj:IFuel):
        self.obj = obj

    def __call__(self):
        return self.obj.set_fuel_amount(
            self.obj.get_fuel_amount() - self.obj.get_fuel_burn_rate()
        )
