from time import strftime
from os import mkdir
from os.path import exists, expanduser
from jinja2 import Environment, PackageLoader

from src.OBJECTS.SCHEMA import SCHEMA

class DATABASE(object):
    def __init__(self, CONNECT):
        self._update = False
        self._name = CONNECT.name
        self._data = CONNECT._extract('select * from columns;')
        self._time = strftime("%Y%m%d-%H%M%S")
        self._dir = f"{expanduser('~')}/.scd/{self._name}"
        self._log_dir = f"{expanduser('~')}/.scd/logs/{self._name}/{self._time}"
        self.check_existance()
        self._env = Environment(loader=PackageLoader('src', 'TEMPLATES'))
        self._schemas = self.construct_schemas(); del self._data
        self._write_change_file()

    def __getitem__(self, item):
        return self._schemas[item]

    def _write_change_file(self):
        if not exists(self._log_dir):
            with open(self._log_dir, "w+") as f:
                template = self._env.get_template('data.change')
                rendered = template.render(DATABASE=self)
                f.write(rendered)

    def check_existance(self):
        if not exists(self._dir):
            self._update = True
            mkdir(f'{self._dir}/')

    def construct_schemas(self):
        unique_schema = self._data['TABLE_SCHEMA'].unique()
        return [                                                        
                 SCHEMA(                                                
                        self,                                           
                        schema,                                         
                        self._data[
                            self._data['TABLE_SCHEMA'] == schema
                                  ]
                        )                                               
                 for schema in unique_schema                            
               ]
