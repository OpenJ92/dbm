from jinja2 import Environment, PackageLoader

from src.OBJECTS.SCHEMA import SCHEMA
from src.OBJECTS.POLICY import POLICY

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
        # what are policy objects and where are they defined? How can 
        # we have these policy objects interact with the execution of the
        # jinja templates? As it stands, we pass self into the template and
        # access, in the case of the model file, the following attributes:
        #
        #       - self._schema._database._name
        #       - self._schema._name
        #       - self._name
        #       - self._columns._name
        #
        # all of which are string attributes. Therefore, in the construction of
        # policies, that which follows from those policies should be constructed
        # or formatted strings or instructions to the objects to skip or embelish.
        #
        # To my mind, upon escaping a level in our DFS, all policies should be in place
        # for that particular object set. 
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
