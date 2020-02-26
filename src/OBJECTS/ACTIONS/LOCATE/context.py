from src.OBJECTS.ACTIONS.LOCATE.DATABASE_LOCATE import DATABASE_LOCATE
from src.OBJECTS.ACTIONS.LOCATE.SCHEMA_LOCATE import SCHEMA_LOCATE
from src.OBJECTS.ACTIONS.LOCATE.TABLE_LOCATE import TABLE_LOCATE
from src.OBJECTS.ACTIONS.LOCATE.COLUMN_LOCATE import COLUMN_LOCATE

class LOCATE(object):
    manage = {
                'DATABASE'  :   DATABASE_LOCATE  ,
                'SCHEMA'    :   SCHEMA_LOCATE    ,
                'TABLE'     :   TABLE_LOCATE     ,
                'COLUMN'    :   COLUMN_LOCATE    ,
             }
    
    def __init__(self, OBJECT):
        self.__bop__ = self.__class__.manage[OBJECT.__class__.__name__](OBJECT)

    def O(self):
        return self.__bop__
