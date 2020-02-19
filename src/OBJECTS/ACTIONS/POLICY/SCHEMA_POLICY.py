from src.OBJECTS.ACTIONS.CHECK.context import CHECK
from src.OBJECTS.ACTIONS.POLICY.DATABASE_POLICY import DATABASE_POLICY

class SCHEMA_POLICY(DATABASE_POLICY):
    population = {}
    def __init__(self, SCHEMA):
        self._check = CHECK.manage[f"{SCHEMA.__class__.__name__}"].population[f"{SCHEMA._name}"]
        DATABASE_POLICY.__init__(self, SCHEMA._parent)
        self.__class__.population[f"{SCHEMA._name}"] = self
        self._parent = DATABASE_POLICY.population[f"{SCHEMA._parent._name}"]
