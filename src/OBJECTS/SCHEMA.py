from os import mkdir
from os.path import exists

from src.OBJECTS.TABLE import TABLE

class SCHEMA(object):
    def __init__(self, DATABASE, name, data):
        self._database = DATABASE
        self._name = name
        self._data = data
        self._policy = self.read_policy()
        self.load_dbt()
        self._tables = self.construct_tables()

    def read_policy(self):
        pass

    def load_dbt(self):
        self._dbt = f'{self._database._dbt}{self._database._name}_{self._name}'
        if not exists(self._dbt):
            mkdir(f'{self._dbt}/')
            mkdir(f'{self._dbt}/base/')
            mkdir(f'{self._dbt}/transformed/')

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

