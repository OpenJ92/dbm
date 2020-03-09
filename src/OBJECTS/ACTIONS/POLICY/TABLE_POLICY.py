from src.OBJECTS.ACTIONS.LOCATE.context import LOCATE
from src.OBJECTS.ACTIONS.POLICY.SCHEMA_POLICY import SCHEMA_POLICY

class TABLE_POLICY(SCHEMA_POLICY):
    population = {}
    def __init__(self, TABLE, env):
        self._locate = LOCATE.manage[f"{TABLE.__class__.__name__}"].population[f"{TABLE._name}"]
        SCHEMA_POLICY.__init__(self, TABLE._parent, env)
        self.__class__.population[f"{TABLE._name}"] = self
        self._parent = SCHEMA_POLICY.population[f"{TABLE._parent._name}"]
