from DATABASE_CHECK import DATABASE_CHECK

class SCHEMA_CHECK(DATABASE_CHECK):
    def __init__(self, SCHEMA):
        DATABASE_CHECK.__init__(SCHEMA._database)
        self._exp = f"{self._exp}/{SCHEMA._name}"
