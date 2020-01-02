from snowflake.connector import connect
from yaml import load, FullLoader
from os.path import expanduser
from pandas import read_sql

class CONNECT(object):
    def __init__(self, name):
        self.name = name
        self._configuration = self._process_configuration()

    def __enter__(self):
        print("__enter__")
        self._connection = connect(**self._configuration[self.name])
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        print("__exit__")
        self._connection.close()

    def _process_configuration(self):
        configuration = f"{expanduser('~')}/.scd/config.yml"
        with open(configuration, 'r') as c:
            return load(c, Loader=FullLoader)

    def _extract(self, sql):
        return read_sql(sql, self._connection)
