from DATABASE_CHECK import DATABASE_CHECK
from SCHEMA_CHECK import SCHEMA_CHECK
from TABLE_CHECK import TABLE_CHECK
from COLUMN_CHECK import COLUMN_CHECK

class CHECK(object):
    manage = {
                'DATABASE'  :   DATABASE_CHECK  ,
                'SCHEMA'    :   SCHEMA_CHECK    ,
                'TABLE'     :   TABLE_CHECK     ,
                'COLUMN'    :   COLUMN_CHECK    ,
             }
    
    def __init__(self, OBJECT):
        self._produce = cls.manage[OBJECT.__class__.__name__](OBJECT)
        __import__('pdb').set_trace()
        self = self._produce
        __import__('pdb').set_trace()

    def __act__(self):
        pass
