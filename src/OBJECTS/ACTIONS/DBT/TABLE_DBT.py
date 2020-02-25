from os.path import exists, expanduser

from src.OBJECTS.ACTIONS.DBT._DBT import _DBT
from src.OBJECTS.ACTIONS.CHECK.context import CHECK
from src.OBJECTS.ACTIONS.POLICY.context import POLICY

class TABLE_DBT(_DBT):
    def __init__(self, TABLE, env):
        _DBT.__init__(env)
        self._check = CHECK.manage[f"{TABLE.__class__.__name__}"].population[f"{TABLE._name}"]
        self._object = TABLE
        self._page = f"{expanduser('~')}/.scd/test/\
                       {database._name}/\
                       {schema._name}/\
                       {table._name}/dbt.sql"
        self._template = self._env.get_template('distill.dbt.sql')
