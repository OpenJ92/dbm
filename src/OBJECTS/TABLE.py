from os import mkdir
from os.path import exists

from src.OBJECTS.COLUMN import COLUMN

class TABLE(object):
    def __init__(self, SCHEMA, name, data):
        self._schema = SCHEMA
        self._name = name
        self._data = data
        self._columns = self.construct_columns(); del self._data
        self.construct_dbt()

    def __getitem__(self, item):
        return self._columns[item]

    def read_policy(self):
        pass

    def construct_dbt(self):
        self._dbt = f'{self._schema._dbt}/base/{self._schema._name}_{self._name}.sql'
        if not exists(self._dbt):
            with open(self._dbt, "w+") as f:
                template = self._schema._database._env.get_template("object_model.sql")
                rendered = template.render(TABLE=self)
                f.write(rendered)

    def construct_columns(self):
        unique_columns = self._data['COLUMN_NAME'].unique()
        return [
                COLUMN(
                        self,
                        column,
                        self._data[
                            self._data['COLUMN_NAME'] == column
                                  ]
                       )
                for column in unique_columns
               ]
