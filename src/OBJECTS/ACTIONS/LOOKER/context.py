from jinja2 import Environment, PackageLoader

from src.OBJECTS.ACTIONS.LOOKER.SCHEMA_LOOKER import SCHEMA_LOOKER
from src.OBJECTS.ACTIONS.LOOKER.TABLE_LOOKER import TABLE_LOOKER
from src.OBJECTS.ACTIONS.IDENTITY import IDENTITY

class LOOKER(object):
    manage = {
                'DATABASE'  :   IDENTITY      ,
                'SCHEMA'    :   IDENTITY      ,
                'TABLE'     :   TABLE_LOOKER  ,
                'COLUMN'    :   IDENTITY      ,
             }

    env = Environment(loader=PackageLoader('src', 'TEMPLATES'))
    
    def __init__(self, OBJECT):
        self.__bop__ = self.__class__.manage[OBJECT.__class__.__name__](OBJECT, self.__class__.env)

    def O(self):
        return self.__bop__
