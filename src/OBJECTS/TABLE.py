from os import mkdir
from os.path import exists
from re import search, compile, findall, MULTILINE, DOTALL

from src.OBJECTS.COLUMN import COLUMN

class TABLE(object):
    def __init__(self, SCHEMA, name, data):
        self._update = False
        self._schema = SCHEMA
        self._name = name
        self._dbt = f'{self._schema._dbt}/base/{self._schema._name}_{self._name}.sql'
        self._read_dbt()
        self._data = data; self._columns = self.construct_columns(); del self._data

    def __getitem__(self, item):
        return self._columns[item]

    def read_policy(self):
        pass

    def read_dbt(self):
        if exists(self._dbt):
            with open(self._dbt) as f:
                a = f.read()
                b = compile(r"renamed.* as (?P<cols>\(.*\))", 
                        MULTILINE|DOTALL)
                b1 = compile(r'".*" as .*,?', 
                        MULTILINE)
                c = search(b, a)
                d = [i.replace('"', '').split(' as ') 
                        for i in findall(b1, c.group(1))]
                self._dbt_conversion = {i[0]: i[1] for i in d}
        else: 
            self.construct_dbt()

    def construct_dbt(self):
        if not exists(self._dbt) or self.update:
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
