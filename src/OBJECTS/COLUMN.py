class COLUMN(object):
    def __init__(self, TABLE, name, data):
        self._table = TABLE
        self._name = name
        self._data = data
        self._policy = self.read_policy()

    def read_policy(self):
        pass
