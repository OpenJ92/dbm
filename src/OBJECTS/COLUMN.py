class COLUMN(object):
    def __init__(self, TABLE, name, data):
        self._update = False
        self._table = TABLE
        self._name = name
        self._data = self.reform_data(data)
        self.check_existance()

    def __getitem__(self, item):
        return self._data[item]

    def __repr__(self):
        return f"""COLUMN(name={self._name},table={self._table._name},schema={self._table._schema._name})"""

    def check_existance(self):
        if self._name not in self._table._read_data
            self._table._update = True
            print(self)

    def reform_data(self, data):
        return {key : value for key, value in data.iloc[0].items()}
