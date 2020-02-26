from src.OBJECTS.ACTIONS.LOCATE.SCHEMA_LOCATE import SCHEMA_LOCATE

class TABLE_LOCATE(SCHEMA_LOCATE):
    population = {}
    def __init__(self, TABLE):
        SCHEMA_LOCATE.__init__(self, TABLE._parent)
        self._exp = f"{self._exp}/{TABLE._name}"
        self.__class__.population[f'{TABLE._name}'] = self
        self._parent = SCHEMA_LOCATE.population[f'{TABLE._parent._name}']
