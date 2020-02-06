from os.path import exists, expanduser

from src.OBJECTS.ACTIONS.CHECK.SCHEMA_CHECK import SCHEMA_CHECK

class TABLE_CHECK(SCHEMA_CHECK):
    population = {}
    def __init__(self, TABLE):
        SCHEMA_CHECK.__init__(self, TABLE._parent)
        self._exp = f"{self._exp}/{TABLE._name}"
        self.__class__.population[f'{TABLE._name}'] = self
        self._parent = SCHEMA_CHECK.population[f'{TABLE._parent._name}']

    def __check__(self):
        self.update = False if exists(self._exp) else (self.__setup__() and self.__update__())

    def __update__(self):
        self._parent.update = True if (not self._parent and self._parent.__update__()) else True
