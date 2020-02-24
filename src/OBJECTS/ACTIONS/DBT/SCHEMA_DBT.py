from src.OBJECTS.ACTIONS.DBT._DBT import _DBT

class SCHEMA_DBT(object):
    def __init__(self, SCHEMA, env):
        _DBT.__init__(env)
        self._page = f"{expanduser('~')}/.scd/test/{database._name}/{schema._name}/dbt.sql"

    def __act__(self):
        pass
