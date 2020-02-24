from src.OBJECTS.ACTIONS.DBT._DBT import _DBT

class TABLE_DBT(object):
    def __init__(self, TABLE, env):
        _DBT.__init__(env)
        self._page = f"{expanduser('~')}/.scd/test/{database._name}/{schema._name}/{table._name}/dbt.sql"

    def __act__(self):
        pass
