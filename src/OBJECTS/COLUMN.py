class COLUMN(object):
    def __init__(self, TABLE, name, data):
        self._table = TABLE
        self._name = name
        self._data = self.reform_data(data)
        self._check_existance()

    def __getitem__(self, item):
        return self._data[item]

    def read_policy(self):
        pass

    def check_existance(self):
        try: 
            self._table._dbt_conversion[self._name]
        except: 
            self._table._update = True

    def reform_data(self, data):
        return {key : value for key, value in data.iloc[0].items()}
