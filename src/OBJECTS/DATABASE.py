from time import strftime
from os import mkdir
from os.path import exists, expanduser
from jinja2 import Environment, PackageLoader

from src.OBJECTS.SCHEMA import SCHEMA

class DATABASE(object):
    def __init__(self, CONNECT):
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
            _schemas::list - list of src.OBJECT.SCHEMA objects

        function: Attribute nessesary state to src.OBJECT.DATABASE.DATABASE
            object, check the existance of such a database in currently stored
            images and construct src.OBJECT.SCHEMA.SCHEMA objects. Once DFS of 
            database objects is complete, write a change file to self._log_dir
        """
        self._name = CONNECT.name
        self._data = CONNECT._extract('select * from columns;')
        self._time = strftime("%Y%m%d-%H%M%S")
        self._dir = f"{expanduser('~')}/.scd/{self._name}"
        self._log_dir = f"{expanduser('~')}/tmp/.scd/data.change"
        self.check_existance()
        self._env = Environment(loader=PackageLoader('src', 'TEMPLATES'))
        self._schemas = self.construct_schemas(); del self._data
        self._write_change_file()

    def __getitem__(self, item):
        """
        __getitem__(self, item)
        item::int

        function: Afford src.OBJECT.DATABASE.DATABASE itterable
            behaviors for use in loops.

        returns - src.OBJECT.SCHEMA.SCHEMA
        """
        return self._schemas[item]

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
                template = self._env.get_template('data.change')
                rendered = template.render(DATABASE=self)
                f.write(rendered)

    def check_existance(self):
        """
        check_existance(self):

        function: If the expected coresponding directory does not 
            exist, Update instance _update variable to True and 
            construct said coresponding directory.
        """
        if not exists(self._dir):
            mkdir(f'{self._dir}/')

    def construct_schemas(self):
        """
        construct_schemas(self)

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
                                  ]
                        )                                               
                 for schema in unique_schema                            
               ]
