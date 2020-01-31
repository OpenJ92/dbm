from os.path import exists
from re import search, compile, findall, MULTILINE, DOTALL

from src.OBJECTS.COLUMN import COLUMN

class TABLE(object):
    def __init__(self, SCHEMA, name, data):
        """
        __init__(self, SCHEMA, name, data):
            SCHEMA::src.OBJECTS.SCHEMA.SCHEMA - schema object defined
            ---@ scd/src/OBJECTS/SCHEMA
            name::string
            data::pandas.DataFrame - Filtered data queried from src.CONNECT object

        attributes:
            _update::bool - Update flag
            _schema::src.OBJECTS.SCHEMA.SCHEMA
            _name::string - Table name
            _data::pandas.DataFrame - Filtered data queried from src.CONNECT object
            _dir::string - File to map table to.
            read_data::list - list of strings of names of columns
            _data::pandas.DataFrame - Filtered data queried from src.CONNECT object
            _columns::list - list of src.OBJECT.COLUMN objects

        function: Attribute nessesary state to src.OBJECT.TABLE.TABLE
            object, check the existance of such a table in currently stored
            images, and construct src.OBJECTS.TABLE.TABLE objects. Upon comp-
            letion of the construction of src.OBJECT.COLUMN.COLUMN objects, if
            any of those columns triggered the _update attribute to trigger, 
            We then construct that file and write the contents of the rendered 
            template to that file.

        returns - self
        """
        self._schema = SCHEMA
        self._name = name
        self._data = data; self._columns = self.construct_columns(); del self._data

    def __getitem__(self, item):
        """
        __getitem__(self, item)
        item::int

        function: Afford src.OBJECT.DATABASE.DATABASE itterable
            behaviors for use in loops.

        returns - src.OBJECT.SCHEMA.SCHEMA
        """
        return self._columns[item]

    def construct_columns(self):
        """
        construct_schemas(self)

        function: find the unique SCHEMA names in the connected 
            DATABASE and instanciate src.OBJECTS.SCHEMA.SCHEMA
            objects for each of those names. See src.OBJECTS.\
            SCHEMA.SCHEMA for further details.

        """
        unique_columns = self._data['COLUMN_NAME'].unique()
        return [
                COLUMN(
                        self,
                        column,
                        self._data[
                            self._data['COLUMN_NAME'] == column
                                  ]
                       )
                for column in unique_columns
               ]
