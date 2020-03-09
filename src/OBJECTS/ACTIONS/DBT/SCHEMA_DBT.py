from os.path import exists, expanduser

from src.OBJECTS.ACTIONS.DBT._DBT import _DBT
from src.OBJECTS.ACTIONS.POLICY.context import POLICY

class SCHEMA_DBT(_DBT):
    def __init__(self, SCHEMA, env):
        _DBT.__init__(self, env)
        self._policy = POLICY.manage[
                                     f"{SCHEMA.__class__.__name__}"
                                    ].population[f"{SCHEMA._name}"]
        self._object = SCHEMA
        self._page = f"{self._policy._locate._exp}/_dbt.sql"
        self._template = self._env.get_template('reform.dbt.schema.yml')
