from src.OBJECTS.ACTIONS.LOCATE.DATABASE_LOCATE import DATABASE_LOCATE

class SCHEMA_LOCATE(DATABASE_LOCATE):
    population = {}
    def __init__(self, SCHEMA):
        DATABASE_LOCATE.__init__(self, SCHEMA._parent)
        self._exp = f"{self._exp}/{SCHEMA._name}"
        self.__class__.population[f'{SCHEMA._name}'] = self
        self._parent = DATABASE_LOCATE.population[f'{SCHEMA._parent._name}']
