from os.path import exists, expanduser

from src.OBJECTS.ACTIONS.DBT._DBT import _DBT

class SCHEMA_DBT(_DBT):
    def __init__(self, SCHEMA, env):
        _DBT.__init__(env)
        self._page = f"{expanduser('~')}/.scd/test/\
                       {database._name}/\
                       {schema._name}/dbt.sql"
        self._template = self._env.get_template('distill.dbt.schema.yml')
