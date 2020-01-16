from os.path import exists
from re import search, compile, findall, MULTILINE, DOTALL

from src.OBJECTS.COLUMN import COLUMN

class TABLE(object):
    def __init__(self, SCHEMA, name, data):
        self._update = False
        self._schema = SCHEMA
        self._name = name
        self._dir = f'{self._schema._dir}/{self._name}.data'
        self.read_data = self._read_data()
        self._data = data; self._columns = self.construct_columns(); del self._data
        self.construct_dir() if self._update else False

    def __getitem__(self, item):
        return self._columns[item]

    def construct_dir(self):
        if not exists(self._dir) or self._update:
            self._schema._update = True
            with open(self._dir, "w+") as f:
                template = self._schema._database._env.get_template('template.data')
                rendered = template.render(TABLE=self)
                f.write(rendered)

    def _read_data(self):
        if exists(self._dir):
            with open(self._dir) as f:
                return f.readlines()
        else:
            return [] 

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
