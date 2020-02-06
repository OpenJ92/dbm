from src.OBJECTS.ACTIONS.CHECK.DATABASE_CHECK import DATABASE_CHECK
from src.OBJECTS.ACTIONS.CHECK.SCHEMA_CHECK import SCHEMA_CHECK
from src.OBJECTS.ACTIONS.CHECK.TABLE_CHECK import TABLE_CHECK
from src.OBJECTS.ACTIONS.CHECK.COLUMN_CHECK import COLUMN_CHECK

class CHECK(object):
    manage = {
                'DATABASE'  :   DATABASE_CHECK  ,
                'SCHEMA'    :   SCHEMA_CHECK    ,
                'TABLE'     :   TABLE_CHECK     ,
                'COLUMN'    :   COLUMN_CHECK    ,
             }
    
    def __init__(self, OBJECT):
        self.__bop__ = self.__class__.manage[OBJECT.__class__.__name__](OBJECT)

    def O(self):
        return self.__bop__
