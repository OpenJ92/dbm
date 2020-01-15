from os import mkdir
from os.path import exists

from src.OBJECTS.TABLE import TABLE
from src.OBJECTS.POLICY import POLICY

class SCHEMA(object):
    def __init__(self, DATABASE, name, data):
        self._update = False
        self._database = DATABASE
        self._name = name
        self._data = data
        self._dir = f'{self._database._dir}/{self._name}'
        self.check_existance()
        self._tables = self.construct_tables(); del self._data
    
    def __getitem__(self, item):
        return self._tables[item]

    def check_existance(self):
        if not exists(self._dir):
            self._update = True
            mkdir(f'{self._dir}')

    def construct_tables(self):
        unique_tables = self._data['TABLE_NAME'].unique()
        return [
                TABLE(
                       self,
                       table,
                       self._data[
                           self._data['TABLE_NAME'] == table
                                 ]
                      )
                for table in unique_tables
               ]
