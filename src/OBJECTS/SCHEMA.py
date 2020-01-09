from os import mkdir
from os.path import exists

from src.OBJECTS.TABLE import TABLE

class SCHEMA(object):
    def __init__(self, DATABASE, name, data):
        self._database = DATABASE
        self._name = name
        self._data = data
        self._policy = self.read_policy()
        self._dbt = f'{self._database._dbt}{self._database._name}_{self._name}'
        self.setup_dbt()
        self._tables = self.construct_tables(); del self._data
        # self.construct_dbt()
    
    def __getitem__(self, item):
        return self._tables[item]

    def read_policy(self):
        pass

    def setup_dbt(self):
        if not exists(self._dbt):
            mkdir(f'{self._dbt}/')
            mkdir(f'{self._dbt}/base/')
            mkdir(f'{self._dbt}/transformed/')

    def construct_dbt(self):
        if not exists(f'{self._dbt}/base/schema.yml'):
            with open(f'{self._dbt}/base/schema.yml', 'w+') as f:
                template = self._database._env.get_template("object_schema.yml")
                rendered = template.render(SCHEMA=self)
                f.write(rendered)

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

