from os.path import exists, expanduser
from os import mkdir

class _CHECK(object):
    def __init__(self, IMAGE_DIR = f"{expanduser('~')}/.scd/test"):
        self._exp = IMAGE_DIR

    def __act__(self):
        self.__check__(); return self

    def __check__(self):
        if not exists(self._exp): 
            self.__setup__()
        else: 
            self.update = False

    def __setup__(self):
        mkdir(self._exp)
        self.__update__()

    def __update__(self):
        self.update = True
        if self._parent: self._parent.__update__()


