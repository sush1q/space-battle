from typing import Any
from .common import *
from abc import ABC, abstractmethod


class IMoveable(ABC):
    @abstractmethod
    def get_position(self, *args):
        pass

    @abstractmethod
    def set_position(self, *args):
        pass
    
    @abstractmethod
    def get_velocity(self, *args):
        pass


class MoveableAdapter(IMoveable):
    position_property = 'position'
    velocity_property = 'velocity'
    
    def __init__(self, obj: UObject) -> None:
        self.obj = obj

    def get_position(self):
        return self.obj.get_property(MoveableAdapter.position_property)

    def get_velocity(self):
        return self.obj.get_property(MoveableAdapter.velocity_property)

    def set_position(self, new_position: Point):
        return self.obj.set_property(MoveableAdapter.position_property, new_position)


class Move(ICommand):
    def __init__(self, obj:IMoveable) -> None:
        self.obj = obj
        
    def __call__(self):
        self.obj.set_position(self.obj.get_position()+self.obj.get_velocity())
