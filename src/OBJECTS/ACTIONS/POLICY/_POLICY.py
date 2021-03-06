from yaml import load, FullLoader
from os.path import exists, expanduser
from os import mkdir

class _POLICY(object):
    def __init__(self, env):
        self._env = env

    def __act__(self):
        self.__read_policy__(); return self

    def __read_policy__(self):
        self.__setup__()
        with open(f"{self._exp}/policy.yml", 'r') as c:
            self.policy = load(c, Loader=FullLoader)

    def __setup__(self):
        if not exists(f"{self._exp}/policy.yml") or self._object.update:
            with open(f"{self._exp}/policy.yml", 'a') as f:
                f.write(self._template.render(OBJECT=self._object))
