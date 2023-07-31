from abc import ABC, abstractmethod


class ISpinable(ABC):
    @abstractmethod
    def do(self, *args):
        pass
