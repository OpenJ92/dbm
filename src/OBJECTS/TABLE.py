from src.OBJECTS.COLUMN import COLUMN

class TABLE(object):
    def __init__(self, SCHEMA, name, data):
        self._schema = SCHEMA
        self._name = name
        self._data = data
        self._columns = self.construct_columns()
        self._policy = self.read_policy()

    def __eq__(self, other):
        pass

    def read_policy(self):
        pass

    def construct_columns(self):
        unique_columns = self._data['COLUMN_NAME'].unique()
        return {
                column
                :
                COLUMN(
                        self,
                        column,
                        self._data[
                            self._data['COLUMN_NAME'] == column
                                  ]
                       )
                for column in unique_columns
                }
