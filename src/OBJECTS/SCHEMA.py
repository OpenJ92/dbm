from os import mkdir
from os.path import exists

from src.OBJECTS.TABLE import TABLE

class SCHEMA(object):
    def __init__(self, DATABASE, name, data):
        """
        __init__(self, DATABASE, name, data):
            DATABASE::src.OBJECTS.DATABASE.DATABASE - database object defined
            ---@ scd/src/OBJECTS/DATABASE
            name::string
            data::pandas.DataFrame - Filtered data queried from src.CONNECT object

        attributes:
            _update::bool - Update flag
            _database::src.OBJECTS.DATABASE.DATABASE 
            _name::string - Schema name
            _data::pandas.DataFrame - Filtered data queried from src.CONNECT object
            _dir::string - Location to map schema to.
            _tables::list - list of src.OBJECT.TABLE objects

        function: Attribute nessesary state to src.OBJECT.SCHEMA.SCHEMA 
            object, check the existance of such a schem a in currently stored
            images, and construct src.OBJECTS.TABLE.TABLE objects.
        """
        self._update = False
        self._database = DATABASE
        self._name = name
        self._data = data
        self._dir = f'{self._database._dir}/{self._name}'
        self.check_existance()
        self._tables = self.construct_tables(); del self._data
    
    def __getitem__(self, item):
        """
        __getitem__(self, item)
        item::int

        function: Afford src.OBJECT.DATABASE.DATABASE itterable
            behaviors for use in loops.

        returns - src.OBJECT.SCHEMA.SCHEMA
        """
        return self._tables[item]

    def check_existance(self):
        """
        check_existance(self):

        function: If the expected coresponding directory does not 
            exist, Update instance _update variable to True and 
            construct said coresponding directory.
        """
        if not exists(self._dir):
            mkdir(f'{self._dir}')

    def construct_tables(self):
        """
        construct_schemas(self)

        function: find the unique SCHEMA names in the connected 
            DATABASE and instanciate src.OBJECTS.SCHEMA.SCHEMA
            objects for each of those names. See src.OBJECTS.\
            SCHEMA.SCHEMA for further details.

        """
        unique_tables = self._data['TABLE_NAME'].unique()
        return [
                TABLE(
                       self,
                       table,
                       self._data[
                           self._data['TABLE_NAME'] == table
                                 ]
                      )
                for table in unique_tables
               ]
