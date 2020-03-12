from src.OBJECTS.ACTIONS.LOCATE.context import LOCATE
from src.OBJECTS.ACTIONS.POLICY.DATABASE_POLICY import DATABASE_POLICY

class SCHEMA_POLICY(DATABASE_POLICY):
    population = {}
    def __init__(self, SCHEMA, env):
        DATABASE_POLICY.__init__(self, SCHEMA._parent, env)
        self._object = SCHEMA
        self._template = env.get_template('reform.policy.yml')
        self._locate = LOCATE.manage[f"{SCHEMA.__class__.__name__}"].population[f"{SCHEMA._name}"]
        self._exp = self._locate._exp
        self.__class__.population[f"{SCHEMA._name}"] = self
        self._parent = DATABASE_POLICY.population[f"{SCHEMA._parent._name}"]
