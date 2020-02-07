from os.path import exists, expanduser

from src.OBJECTS.ACTIONS.CHECK.TABLE_CHECK import TABLE_CHECK

class COLUMN_CHECK(TABLE_CHECK):
    population = {}
    def __init__(self, COLUMN):
        TABLE_CHECK.__init__(self, COLUMN._parent)
        self._exp = f"{self._exp}/{COLUMN._name}"
        self.__class__.population[f'{COLUMN._name}'] = self
        self._parent = TABLE_CHECK.population[f'{COLUMN._parent._name}']
