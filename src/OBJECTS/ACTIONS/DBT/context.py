from jinja2 import Environment, PackageLoader

from src.OBJECTS.ACTIONS.DBT.SCHEMA_DBT import SCHEMA_DBT
from src.OBJECTS.ACTIONS.DBT.TABLE_DBT import TABLE_DBT
from src.OBJECTS.ACTIONS.IDENTITY import IDENTITY

class DBT(object):
    manage = {
                'DATABASE'  :   IDENTITY      ,
                'SCHEMA'    :   SCHEMA_DBT    ,
                'TABLE'     :   TABLE_DBT     ,
                'COLUMN'    :   IDENTITY      ,
             }

    env = Environment(loader=PackageLoader('src', 'TEMPLATES'))
    
    def __init__(self, OBJECT):
        self.__bop__ = self.__class__.manage[OBJECT.__class__.__name__](OBJECT, self.__class__.env)

    def O(self):
        return self.__bop__
