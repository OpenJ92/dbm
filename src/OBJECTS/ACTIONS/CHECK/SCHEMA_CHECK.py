from os.path import exists, expanduser

from src.OBJECTS.ACTIONS.CHECK.DATABASE_CHECK import DATABASE_CHECK

class SCHEMA_CHECK(DATABASE_CHECK):
    population = {}
    def __init__(self, SCHEMA):
        DATABASE_CHECK.__init__(self, SCHEMA._parent)
        self._exp = f"{self._exp}/{SCHEMA._name}"
        self.__class__.population[f'{SCHEMA._name}'] = self
        self._parent = DATABASE_CHECK.population[f'{SCHEMA._parent._name}']

    def __check__(self):
        self.update = False if exists(self._exp) else (self.__setup__() and self.__update__())

    def __update__(self):
        self._parent.update = True if (not self._parent and self._parent.__update__()) else True
