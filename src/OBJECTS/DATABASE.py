from os import mkdir
from os.path import exists, expanduser
from jinja2 import Environment, PackageLoader

from src.OBJECTS.SCHEMA import SCHEMA
from src.OBJECTS.POLICY import POLICY

class DATABASE(object):
    def __init__(self, CONNECT):
        self._update = False
        self._name = CONNECT.name
        self._data = CONNECT._extract('select * from columns;')
        # note to self. Replace dotfile with S3 bucket
        self._dir = f"{expanduser('~')}/.scd/{self._name}"
        self.check_existance()
        self._env = Environment(loader=PackageLoader('src', 'TEMPLATES'))
        self._schemas = self.construct_schemas(); del self._data

    def __getitem__(self, item):
        return self._schemas[item]

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
