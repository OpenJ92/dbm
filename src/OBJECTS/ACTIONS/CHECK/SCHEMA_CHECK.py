from src.OBJECTS.ACTIONS.CHECK.DATABASE_CHECK import DATABASE_CHECK

class SCHEMA_CHECK(DATABASE_CHECK):
    population = {}
    def __init__(self, SCHEMA):
        DATABASE_CHECK.__init__(self, SCHEMA._parent)
        self._exp = f"{self._exp}/{SCHEMA._name}"
        self.__class__.population[f'{SCHEMA._name}'] = self
        self._parent = DATABASE_CHECK.population[f'{SCHEMA._parent._name}']
