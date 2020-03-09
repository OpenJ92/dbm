from os.path import exists

class _DBT(object):
    def __init__(self, env):
        self._env = env

    def __act__(self):
        if not exists(self._page):
            with open(self._page, 'w') as f:
                f.write(self._template.render(OBJECT=self._object))
        return self
