from os.path import exists, expanduser

from src.OBJECTS.ACTIONS.CHECK._CHECK import _CHECK

class DATABASE_CHECK(_CHECK):
    population = {}
    def __init__(self, DATABASE):
        _CHECK.__init__(self)
        self._exp = f"{self._exp}/{DATABASE._name}"
        self.__class__.population[f'{DATABASE._name}'] = self
        self._parent = None
