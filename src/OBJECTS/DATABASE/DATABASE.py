from src.OBJECTS.DATABASE.SCHEMA import SCHEMA 

class DATABASE(object):
    def __init__(self, CONNECT, ACTION = []):
        """
        __init__(self):
            CONNECT::src.CONNECT - connect object defined @ scd/src/CONNECT

        attributes:
            _name::string - Database name
            _data::pandas.DataFrame - Data queried from src.CONNECT object
            _time::string - Time of execution for log name
            _dir::string - Location to map database to.
            _log_dir::string - Location to output unseen columns
            _env::jinja2.environment.Environment - template manager
            _children::list - list of src.OBJECT.SCHEMA objects

        function: Attribute nessesary state to src.OBJECT.DATABASE.DATABASE
            object, check the existance of such a database in currently stored
            images and construct src.OBJECT.SCHEMA.SCHEMA objects. Once DFS of 
            database objects is complete, write a change file to self._log_dir
        """
        self._name = CONNECT.name
        self._data = CONNECT._extract('select * from columns;')
        self._ACTION = ACTION
        self._actions = {action.__name__ : action(self).O().__act__() for action in ACTION}
        self._children = self.construct_children(); del self._data

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
        construct_children(self)

        function: find the unique SCHEMA names in the connected 
            DATABASE and instanciate src.OBJECTS.SCHEMA.SCHEMA
            objects for each of those names. See src.OBJECTS.\
            SCHEMA.SCHEMA for further details.

        """
        unique_schema = self._data['TABLE_SCHEMA'].unique()
        return [                                                        
                 SCHEMA(                                                
                        self,                                           
                        schema,                                         
                        self._data[
                            self._data['TABLE_SCHEMA'] == schema
                                  ],
                        self._ACTION
                        )                                               
                 for schema in unique_schema
               ]
