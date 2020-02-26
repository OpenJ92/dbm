from src.OBJECTS.ACTIONS.LOCATE.TABLE_LOCATE import TABLE_LOCATE

class COLUMN_LOCATE(TABLE_LOCATE):
    population = {}
    def __init__(self, COLUMN):
        TABLE_LOCATE.__init__(self, COLUMN._parent)
        self._exp = f"{self._exp}/{COLUMN._name}"
        self.__class__.population[f'{COLUMN._name}'] = self
        self._parent = TABLE_LOCATE.population[f'{COLUMN._parent._name}']
