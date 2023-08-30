from server import *


class IoC:
    strategy = IoC.default_strategy
    
    @staticmethod
    def resolve(key: str, *args):
        # return globals()[key](args)
        return IoC.strategy(key, *args)

    def default_strategy(cls, key, *args):
        if key == 'IoC.setup_strategy':
            return SetupStrategy(*args)
        elif key == 'IoC.default':
            return cls.default_strategy
        else:
            raise Exception('Invalid IoC dependency')


class SetupStrategy(ICommand):
    def __init__(self, *args):
        # self.obj = obj
        self.args = args

    def __call__(self):
        # return self.obj()
        pass

