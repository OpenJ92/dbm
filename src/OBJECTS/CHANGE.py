class CHANGE(object):
    @classmethod
    def DATABASE(cls, OBJECT):
        return cls(OBJECT)

    @classmethod
    def SCHEMA(cls, OBJECT):
        return cls(OBJECT)

    @classmethod
    def TABLE(cls, OBJECT):
        return cls(OBJECT)

    @classmethod
    def COLUMN(cls, OBJECT):
        return cls(OBJECT)

    constructors = {
                        'DATABASE': cls.DATABASE,
                        'SCHEMA'  : cls.SCHEMA,
                        'TABLE'   : cls.TABLE,
                        'COLUMN'  : cls.COLUMN
                    }

    def __init__(OBJECT):
        self = cls.constructors[OBJECT.__class__.__name__](OBJECT)

