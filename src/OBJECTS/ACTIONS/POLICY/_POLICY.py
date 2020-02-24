from yaml import load, FullLoader
from os.path import exists, expanduser
from os import mkdir

class _POLICY(object):
    def __init__(self):
        self.__get_location__()

    def __act__(self):
        self.__read_policy__(); return self

    def __read_policy__(self):
        self.__setup__()
        with open(f"{self._exp}/policy", 'r') as c:
            self.policy = load(c, Loader=FullLoader)

    def __setup__(self):
        open(f"{self._exp}/policy", 'a').close()

    def __get_location__(self):
        self._exp = self._check._exp

