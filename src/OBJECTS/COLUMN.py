class COLUMN(object):
    def __init__(self, TABLE, name, data):
        self._table = TABLE
        self._name = name
        self._data = data
        self._policy = self.read_policy()
        print(self._name, self._table._name, self._table._schema._name)

    def read_policy(self):
        pass
