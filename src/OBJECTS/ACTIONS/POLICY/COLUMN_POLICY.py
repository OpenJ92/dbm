from src.OBJECTS.ACTIONS.LOCATE.context import LOCATE
from src.OBJECTS.ACTIONS.POLICY.TABLE_POLICY import TABLE_POLICY

class COLUMN_POLICY(TABLE_POLICY):
    population = {}
    def __init__(self, COLUMN, env):
        self._check = LOCATE.manage[f"{COLUMN.__class__.__name__}"].population[f"{COLUMN._name}"]
        TABLE_POLICY.__init__(self, COLUMN._parent, env)
        self.__class__.population[f"{COLUMN._name}"] = self
        self._parent = TABLE_POLICY.population[f"{COLUMN._parent._name}"]
