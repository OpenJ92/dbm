from src.OBJECTS.DATABASE.TABLE import TABLE

class SCHEMA(object):
    def __init__(self, DATABASE, name, data, ACTION = [], POST_ACTION = []):
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
            _children::list - list of src.OBJECT.TABLE objects

        function: Attribute nessesary state to src.OBJECT.SCHEMA.SCHEMA 
            object, check the existance of such a schem a in currently stored
            images, and construct src.OBJECTS.TABLE.TABLE objects.
        """
        self._parent = DATABASE
        self._name = name
        self._data = data
        self._ACTION = ACTION
        self._POST_ACTION = POST_ACTION
        self._actions = {action.__name__ : action(self).O().__act__() for action in ACTION}
        self._children = self.construct_children(); del self._data
        self._post_actions = {action.__name__ : action(self).O().__act__() for action in POST_ACTION}
    
    def __getitem__(self, item):
        """
        __getitem__(self, item)
        item::int

        function: Afford src.OBJECT.DATABASE.DATABASE itterable
            behaviors for use in loops.

        returns - src.OBJECT.SCHEMA.SCHEMA
        """
        return self._children[item]

    def construct_children(self):
        """
        construct_schemas(self)

        function: find the unique SCHEMA names in the connected 
            DATABASE and instanciate src.OBJECTS.SCHEMA.SCHEMA
            objects for each of those names. See src.OBJECTS.\
            SCHEMA.SCHEMA for further details.

        """
        unique_children = self._data['TABLE_NAME'].unique()
        return [
                TABLE(
                       self,
                       table,
                       self._data[
                           self._data['TABLE_NAME'] == table
                                 ],
                        self._ACTION,
                        self._POST_ACTION
                      )
                for table in unique_children
               ]
