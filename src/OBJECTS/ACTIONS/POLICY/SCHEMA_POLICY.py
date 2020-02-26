from src.OBJECTS.ACTIONS.LOCATE.context import LOCATE
from src.OBJECTS.ACTIONS.POLICY.DATABASE_POLICY import DATABASE_POLICY

class SCHEMA_POLICY(DATABASE_POLICY):
    population = {}
    def __init__(self, SCHEMA, env):
        self._check = LOCATE.manage[f"{SCHEMA.__class__.__name__}"].population[f"{SCHEMA._name}"]
        DATABASE_POLICY.__init__(self, SCHEMA._parent, env)
        self.__class__.population[f"{SCHEMA._name}"] = self
        self._parent = DATABASE_POLICY.population[f"{SCHEMA._parent._name}"]
