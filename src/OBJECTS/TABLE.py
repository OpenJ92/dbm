from os import mkdir
from os.path import exists

from src.OBJECTS.COLUMN import COLUMN

class TABLE(object):
    def __init__(self, SCHEMA, name, data):
        self._schema = SCHEMA
        self._name = name
        self._data = data
        self._dbt = f'{self._schema._dbt}/base/{self._schema._name}_{self._name}.sql'
        self._columns = self.construct_columns()
        self.load_dbt()

    def read_policy(self):
        pass

    def construct_dbt(self):
        with open(self._dbt, "w+") as f:
            template = self._schema._database._env.get_template("model.sql")
            #rendered = template.render(self) (make this happen)
            rendered = template.render(
                         TABLE_CATALOG=self._schema._database._name,
                         TABLE_SCHEMA=self._schema._name,
                         TABLE_NAME=self._name,
                         COLUMN_NAME=self._data['COLUMN_NAME']
                                      )
            f.write(rendered)

    def load_dbt(self):
        try:
            f = open(self._dbt)
            return f.read()
        except IOError:
            # construct the file
            self.construct_dbt()

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
