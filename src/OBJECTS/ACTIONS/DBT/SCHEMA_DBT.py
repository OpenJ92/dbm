from os.path import exists, expanduser

from src.OBJECTS.ACTIONS.DBT._DBT import _DBT
from src.OBJECTS.ACTIONS.CHECK.context import CHECK
from src.OBJECTS.ACTIONS.POLICY.context import POLICY

class SCHEMA_DBT(_DBT):
    def __init__(self, SCHEMA, env):
        _DBT.__init__(env)
        self._check = CHECK.manage[f"{SCHEMA.__class__.__name__}"].population[f"{SCHEMA._name}"]
        self._object = SCHEMA
        self._page = f"{expanduser('~')}/.scd/test/\
                       {database._name}/\
                       {schema._name}/dbt.sql"
        self._template = self._env.get_template('distill.dbt.schema.yml')
