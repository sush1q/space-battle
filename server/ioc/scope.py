
class Scope:
    def __init__(self, dependecies, parent: 'Scope') -> None:
        self.dependencies = dependecies
        self.parent = parent
    
    def resolve(self, key, *args):
        if (self.dependencies.get(key,)):
            return dependency_resolver(args)
        else:
            self.parent.resolve(key, args)
