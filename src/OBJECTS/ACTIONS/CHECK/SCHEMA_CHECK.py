from src.OBJECTS.ACTIONS.CHECK.DATABASE_CHECK import DATABASE_CHECK

class SCHEMA_CHECK(DATABASE_CHECK):
    def __init__(self, SCHEMA):
        DATABASE_CHECK.__init__(self, SCHEMA._parent)
        self._exp = f"{self._exp}/{SCHEMA._name}"
