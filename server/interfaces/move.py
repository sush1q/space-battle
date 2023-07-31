from abc import ABC, abstractmethod


class IMoveable(ABC):
    @abstractmethod
    def do(self, *args):
        pass
