from .common import *
from abc import ABC, abstractmethod


class Spin:
    def __init__(self, obj:'ISpinable') -> None:
        self.obj = obj
        
    def __call__(self):
        self.obj.set_direction(
            (self.obj.get_direction()+self.obj.get_angular_velocity())%self.obj.get_directions_number()
        )


class ISpinable(ABC):
    @abstractmethod
    def get_direction(self):
        pass
    
    @abstractmethod
    def get_directions_number(self):
        pass

    @abstractmethod
    def get_angular_velocity(self):
        pass
    
    @abstractmethod
    def set_direction(self, *args):
        pass


class SpinableAdapter(ISpinable):
    direction_property = 'direction'
    directions_number_property = 'directions_number'
    angular_velocity = 'angular_velocity'
    
    def __init__(self, obj: UObject) -> None:
        self.obj = obj
        
    def get_direction(self):
        return self.obj.get_property(SpinableAdapter.direction_property)
    
    def get_directions_number(self):
        return self.obj.get_property(SpinableAdapter.directions_number_property)
    
    def get_angular_velocity(self):
        return self.obj.get_property(SpinableAdapter.angular_velocity)
    
    def set_direction(self, new_direction):
        return self.obj.set_property(SpinableAdapter.direction_property, new_direction)
