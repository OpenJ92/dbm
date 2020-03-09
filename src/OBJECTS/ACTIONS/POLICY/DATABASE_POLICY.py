from src.OBJECTS.ACTIONS.LOCATE.context import LOCATE
from src.OBJECTS.ACTIONS.POLICY._POLICY import _POLICY

class DATABASE_POLICY(_POLICY):
    population = {}
    def __init__(self, DATABASE, env):
        self._locate = LOCATE.manage[f"{DATABASE.__class__.__name__}"].population[f"{DATABASE._name}"]
        _POLICY.__init__(self, env)
        self.__class__.population[f"{DATABASE._name}"] = self
        self._parent = None 
