from TABLE_CHECK import TABLE_CHECK

class COLUMN_CHECK(TABLE_CHECK):
    def __init__(self, COLUMN):
        TABLE_CHECK.__init__(COLUMN._table)
        self._exp = f"{self._exp}/{COLUMN._name}"

