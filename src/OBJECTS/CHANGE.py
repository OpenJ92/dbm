from os.path import exists
from os import mkdir, listdir

class CHANGE(object):
    @classmethod
    def DATABASE(cls, OBJECT):
        WHERE = f"{expanduser('~')}/.scd/"
        return cls(OBJECT, WHERE)

    @classmethod
    def SCHEMA(cls, OBJECT):
        WHERE = f"{expanduser('~')}/.scd/{OBJECT._database._name}/"
        return cls(OBJECT, WHERE)

    @classmethod
    def TABLE(cls, OBJECT):
        WHERE = f"{expanduser('~')}/.scd/{OBJECT._schema._database._name}/\
                                         {OBJECT._schema._name}"
        return cls(OBJECT, WHERE)

    @classmethod
    def COLUMN(cls, OBJECT):
        WHERE = f"{expanduser('~')}/.scd/{OBJECT._table._schema._database._name}/\
                                         {OBJECT._table._schema._name}/\
                                         {OBJECT._table._name}"
        # CHECK = check fuction??
        return cls(OBJECT, WHERE)

    LOG_DIR = f"{expanduser('~')}/tmp/.scd/data.change"
    CONSTRUCTORS = {
                        'DATABASE': cls.DATABASE,
                        'SCHEMA'  : cls.SCHEMA,
                        'TABLE'   : cls.TABLE,
                        'COLUMN'  : cls.COLUMN
                    }

    def __init__(OBJECT, WHERE=None, HOW=None):
        self = cls.CONSTRUCTORS[OBJECT.__class__.__name__](OBJECT)

    def _existance(self):
        pass

    def _read(self):
        pass

