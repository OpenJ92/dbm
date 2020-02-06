from src.OBJECTS.ACTIONS.CHECK.SCHEMA_CHECK import SCHEMA_CHECK

class TABLE_CHECK(SCHEMA_CHECK):
    def __init__(self, TABLE):
        SCHEMA_CHECK.__init__(self, TABLE._parent)
        self._exp = f"{self._exp}/{TABLE._name}"
