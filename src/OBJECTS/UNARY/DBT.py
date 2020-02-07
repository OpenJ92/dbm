from jinja2 import Environment, PackageLoader
from os.path import exists, expanduser

class DBT(object):
    def __init__(self, DATABASE):
        self._env = Environment(loader=PackageLoader('src', 'TEMPLATES'))
        self._write_dbt_file(DATABASE)

    def _write_dbt_file(self, database):
        template = self._env.get_template('distill.dbt.sql')
        for schema in database:
            for table in schema:
                page = f"{expanduser('~')}/.scd/test/{database._name}/{schema._name}/{table._name}/dbt.sql"
                if not exists(page):
                    with open(page, 'w') as f:
                        rendered = template.render(TABLE=table)
                        f.write(rendered)
                        print(rendered)

    def _read_policy(self):
        pass

