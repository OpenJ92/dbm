from os.path import exists, expanduser
from os import mkdir

class _CHECK(object):
    def __init__(self, IMAGE_DIR = f"{expanduser('~')}/.scd/test"):
        self._exp = IMAGE_DIR

    def __act__(self):
        self.__check__(); return self

    def __check__(self):
        False if exists(self._exp) else (self.__setup__() and self.__update__())

    def __update__(self):
        __import__('pdb').set_trace()
        self.update = True if (not self._parent and self._parent.__update__()) else True

    def __setup__(self):
        mkdir(self._exp); open(f"{self._exp}/policy", 'a').close()
        return True

