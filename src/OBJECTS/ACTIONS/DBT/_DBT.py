class _DBT(object):
    def __init__(self, env):
        self._env = env

    def __act__(self):
        if not exists(self._page):
            with open(self._page, 'w') as f:
                rendered = template.render(TABLE=table)
                f.write(rendered)
