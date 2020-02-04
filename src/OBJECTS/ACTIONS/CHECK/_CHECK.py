class _CHECK(object):
    def __init__(self, IMAGE_DIR = "{expanduser('~')}/.scd/"):
        self._exp = IMAGE_DIR

    def __act__(self):
        self.__check__(); return self

    def __check__(self):
        self.update = False if exist(self._exp) else self.__setup__()

    def __setup__(self):
        mkdir(self._exp); open(f"{self._exp}/policy", 'a').close()
        return True

