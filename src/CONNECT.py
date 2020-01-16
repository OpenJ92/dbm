from snowflake.connector import connect
from yaml import load, FullLoader
from os.path import expanduser
from pandas import read_sql

class CONNECT(object):
    def __init__(self, name):
        """
        __init__(self, name):
        name::string - Name of database to connect to. Direct
                        coresompndance to the outer most layer 
                        of ~/.scd/config.yml dictionary.

        
        function - Store name of database connected to and load
            make connection to affermentioned database.

        returns - self
        """
        self.name = name
        self._configuration = self._process_configuration()

    def __enter__(self):
        """
        __enter__(self):

        function - Unpack configuration credentials for given database
            name and store into instance _connection variable. For use
            with python context manager element.

        returns - self
        """
        self._connection = connect(**self._configuration[self.name])
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        """
        __exit__(self):

        function - Close connection to given database. For use 
            with python context manager element.

        returns - None
        """
        self._connection.close()

    def _process_configuration(self):
        """
        _process_configuration(self):

        function: Through the use of yaml.load function and the 
            FullLoader flag, process .scd/config.yml file into
            python dictionary. For use in the __enter__ method.

        returns - dict
        """
        configuration = f"{expanduser('~')}/.scd/config.yml"
        with open(configuration, 'r') as c:
            return load(c, Loader=FullLoader)

    def _extract(self, sql):
        """
        _extract(self, sql):
        sql::string - sql statement to execute on database

        function: Pull data from database into pandas DataFrame
            object. For our purpose, this will be used to query
            the snowflake information schema view of columns.

        returns - pandas.DataFrame
        """
        return read_sql(sql, self._connection)
