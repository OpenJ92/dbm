class COLUMN(object):
    def __init__(self, TABLE, name, data):
        self._table = TABLE
        self._name = name
        self._data = self.reform_data(data)
        self._policy = self.read_policy()

    def __getitem__(self, item):
        return self._data[item]

    def read_policy(self):
        pass

    def reform_data(self, data):
        return {key : value for key, value in data.iloc[0].items()}


