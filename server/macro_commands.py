from .interfaces import *
from .event_loop import *


class MacroCommand(ICommand):
    def __init__(self, *args:ICommand):
        self.obj = args

    def __call__(self):
        for cmd in self.obj:
            try:
                cmd()
            except:
                raise CommandException

class MoveAndBurnFuelAdapter(MoveableAdapter, FuelAdapter):
    pass

class MoveAndBurnFuel(MacroCommand):
    def __init__(self, obj):
        self.obj = obj
        MacroCommand.__init__(self, CheckFuel(obj), Move(obj), BurnFuel(obj))
