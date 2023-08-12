from .interfaces import *
from .logger import *
from .event_loop import *


class ExceptionHandler:
    store = None

    @classmethod
    def _handled(cls, exception_type, command) -> UObject:
        return UObject(
            {
            'exception_type': exception_type,
            'command': command
            }
        )

    @classmethod
    def handle(cls, exception, command) -> ICommand:
        exc_type = type(exception).__name__
        cmd_type = type(command).__name__
        return cls.store[cmd_type][exc_type](cls._handled(exc_type, command))

class ExceptionLogger(ICommand):
    def __init__(self, obj):
        self.obj = obj

    def __call__(self):
        Logger.log(f'Exception: <{self.obj.get_property("exception_type")}> of Command <{self.obj.get_property("command")}> has been raised')

class RepeatCommand(ICommand):
    def __init__(self, obj):
        self.obj = obj

    def __call__(self):
        self.obj.get_property("command")()

class DoubleRepeatCommand(RepeatCommand):
    pass
