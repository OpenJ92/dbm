from jinja2 import Environment, PackageLoader

from src.OBJECTS.SCHEMA import SCHEMA

class DATABASE(object):
    def __init__(self, CONNECT, dbt='../dbt/models/'):
        self._name = CONNECT.name
        self._data = CONNECT._extract('select * from columns;')
        self._dbt = dbt
        self._env = Environment(loader=PackageLoader('src', 'TEMPLATES'))
        self._schemas = self.construct_schemas(); del self._data

    def __getitem__(self, item):
        return self._schemas[item]

    def read_policy(self):
        pass

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
