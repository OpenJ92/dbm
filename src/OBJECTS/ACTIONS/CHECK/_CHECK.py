from os.path import exists, expanduser
from os import mkdir

class _CHECK(object):
    def __init__(self, IMAGE_DIR = f"{expanduser('~')}/.scd/test"):
        self._exp = IMAGE_DIR

    def __act__(self):
        self.__check__(); return self

    def __setup__(self):
        mkdir(self._exp); open(f"{self._exp}/policy", 'a').close()
        return True

