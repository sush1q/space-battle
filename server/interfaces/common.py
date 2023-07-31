from abc import ABC, abstractmethod


class Point:
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y
        
    def __add__(self, point: 'Point'):
        self.x += point.x
        self.y += point.y
        return self
    
    def __sub__(self, point: 'Point'):
        self.x -= point.x
        self.y -= point.y
        return self

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, tuple):
            raise NotImplementedError
        is_x_eq = self.x == __value[0]
        is_y_eq = self.y == __value[1]
        return is_x_eq and is_y_eq


class IObject(ABC):
    @abstractmethod
    def get_property(self, name):
        pass
    
    @abstractmethod
    def set_property(self, key, value):
        pass
    
class UObject(IObject):
    def __init__(self, obj) -> None:
        self.obj = obj
    
    def get_property(self, name):
        return self.obj[name]
    
    def set_property(self, key, value):
        self.obj[key] = value
