from time import strftime
from os import mkdir
from os.path import exists, expanduser
from jinja2 import Environment, PackageLoader

class CHANGE_REPORT(object):
    def __init__(self, DATABASE):
        self._time = strftime("%Y%m%d-%H%M%S")
        self._log_dir = f"{expanduser('~')}/tmp/.scd/data.change"
        self._env = Environment(loader=PackageLoader('src', 'TEMPLATES'))
        self._database = DATABASE
        self._write_change_file()

    def _write_change_file(self):
        """
        _write_change_file(self):

        function - Checks the existance of _log_directory. If it
            does not exist, We then construct that file and write
            the contents of the rendered template to that file. 
            See jinja2 src.TEMPLATES.data.change or jinja2 docs
            for more information. If it does exist, do nothing.

        returns - None
        """
        if not exists(self._log_dir):
            with open(self._log_dir, "w+") as f:
                template = self._env.get_template('distill.data.change')
                rendered = template.render(DATABASE=self._database)
                f.write(rendered)


