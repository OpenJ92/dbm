from src.OBJECTS.ACTIONS.LOOKER._LOOKER import _LOOKER
from src.OBJECTS.ACTIONS.POLICY.context import POLICY

class TABLE_LOOKER(_LOOKER):
    def __init__(self, TABLE, env):
        _LOOKER.__init__(self, env)
        self._policy = POLICY.manage[
                                     f"{TABLE.__class__.__name__}"
                                    ].population[f"{TABLE._name}"]
        self._object = TABLE
        self._page = f"{self._policy._locate._exp}/looker.view.lkml"
        self._template = self._env.get_template('reform.looker.model.view.lkml')
