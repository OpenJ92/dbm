from src.OBJECTS.TABLE import TABLE

class SCHEMA(object):
    def __init__(self, DATABASE, name, data):
        self._database = DATABASE
        self._name = name
        self._data = data
        self._tables = self.construct_tables()
        self._policy = self.read_policy()

    def read_policy(self):
        pass

    def construct_tables(self):
        unique_tables = self._data['TABLE_NAME'].unique()
        return {
                table
                :
                TABLE(
                       self,
                       table,
                       self._data[
                           self._data['TABLE_NAME'] == table
                                 ]
                      )
                for table in unique_tables
                }

