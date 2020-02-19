from src.OBJECTS.ACTIONS.CHECK.DATABASE_POLICY import DATABASE_POLICY
from src.OBJECTS.ACTIONS.CHECK.SCHEMA_POLICY import SCHEMA_POLICY
from src.OBJECTS.ACTIONS.CHECK.TABLE_POLICY import TABLE_POLICY
from src.OBJECTS.ACTIONS.CHECK.COLUMN_POLICY import COLUMN_POLICY

class POLICY(object):
    manage = {
                'DATABASE'  :   DATABASE_POLICY  ,
                'SCHEMA'    :   SCHEMA_POLICY    ,
                'TABLE'     :   TABLE_POLICY     ,
                'COLUMN'    :   COLUMN_POLICY    ,
             }
    
    def __init__(self, OBJECT):
        self.__bop__ = self.__class__.manage[OBJECT.__class__.__name__](OBJECT)

    def O(self):
        return self.__bop__
