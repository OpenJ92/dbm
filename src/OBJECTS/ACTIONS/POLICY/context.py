from jinja2 import Environment, PackageLoader

from src.OBJECTS.ACTIONS.POLICY.DATABASE_POLICY import DATABASE_POLICY
from src.OBJECTS.ACTIONS.POLICY.SCHEMA_POLICY import SCHEMA_POLICY
from src.OBJECTS.ACTIONS.POLICY.TABLE_POLICY import TABLE_POLICY
from src.OBJECTS.ACTIONS.POLICY.COLUMN_POLICY import COLUMN_POLICY

class POLICY(object):
    manage = {
                'DATABASE'  :   DATABASE_POLICY  ,
                'SCHEMA'    :   SCHEMA_POLICY    ,
                'TABLE'     :   TABLE_POLICY     ,
                'COLUMN'    :   COLUMN_POLICY    ,
             }

    env = Environment(loader=PackageLoader('src', 'TEMPLATES'))
    
    def __init__(self, OBJECT):
        print("CONTEXT FACTORY")
        self.__bop__ = self.__class__.manage[OBJECT.__class__.__name__](OBJECT, self.__class__.env)

    def O(self):
        return self.__bop__
