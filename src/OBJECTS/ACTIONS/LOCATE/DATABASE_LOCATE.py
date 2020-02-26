from src.OBJECTS.ACTIONS.LOCATE._LOCATE import _LOCATE

class DATABASE_LOCATE(_LOCATE):
    population = {}
    def __init__(self, DATABASE):
        _LOCATE.__init__(self)
        self._exp = f"{self._exp}/{DATABASE._name}"
        self.__class__.population[f'{DATABASE._name}'] = self
        self._parent = None
