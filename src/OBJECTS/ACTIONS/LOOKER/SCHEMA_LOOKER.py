from src.OBJECTS.ACTIONS.LOOKER._LOOKER import _LOOKER
from src.OBJECTS.ACTIONS.POLICY.context import POLICY

class SCHEMA_LOOKER(_LOOKER):
    def __init__(self, SCHEMA, env):
        _LOOKER.__init__(self, env)
        self._policy = POLICY.manage[
                                     f"{SCHEMA.__class__.__name__}"
                                    ].population[f"{SCHEMA._name}"]
        self._object = SCHEMA
        self._page = f"{self._policy._locate._exp}/looker.model.lkml"
        self._template = self._env.get_template('')
