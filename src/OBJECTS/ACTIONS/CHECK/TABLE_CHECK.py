from os.path import exist
from os import mkdir

from _CHECK import _CHECK

class TABLE_CHECK(_CHECK):
    def __init__(self, TABLE):
        _CHECK.__init__()
        self._exp = f"{self._IMAGE_DIR}/{TABLE._schema._database.name}/\
                                        {TABLE._schema._name}/\
                                        {TABLE._name}"

    def __act__(self):
        self.__check__(); return self

    def __check__(self):
        self.update = False if exist(self._exp) else self.__setup__()

    def __setup__(self):
        mkdir(self._exp); open(f"{self._exp}/policy", 'a').close()
        return True

