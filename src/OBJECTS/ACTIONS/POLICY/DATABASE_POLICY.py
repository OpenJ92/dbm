from src.OBJECTS.ACTIONS.CHECK.context import CHECK
from src.OBJECTS.ACTIONS.POLICY._POLICY import _POLICY

class DATABASE_POLICY(_POLICY):
    population = {}
    def __init__(self, DATABASE):
        _POLICY.__init__(self, DATABASE._parent)
        self._check = CHECK.manage[f"{DATABASE.__class__.__name__}"].population[f"{DATABASE._name}"]
        self.__class__.population[f"{DATABASE._name}"] = self
        self._parent = _POLICY.population[f"{DATABASE._parent._name}"]
