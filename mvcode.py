# DATABASE.py
        self._update = False
        self._time = strftime("%Y%m%d-%H%M%S")
        self._dir = f"{expanduser('~')}/.scd/{self._name}"
        self._log_dir = f"{expanduser('~')}/tmp/.scd/data.change"
        self.check_existance()
        self._env = Environment(loader=PackageLoader('src', 'TEMPLATES'))
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

# SCHEMA.py
        self._update = False
        self._dir = f'{self._database._dir}/{self._name}'
        self.check_existance()

    def check_existance(self):
        """
        check_existance(self):

        function: If the expected coresponding directory does not 
            exist, Update instance _update variable to True and 
            construct said coresponding directory.
        """
        if not exists(self._dir):
            mkdir(f'{self._dir}')

# TABLE.py
        self._update = False
        self._dir = f'{self._schema._dir}/{self._name}.data'
        self.read_data = self._read_data()
        self.construct_dir()

    def construct_dir(self):
        """
        construct_dir(self):

        function: check to see if table file exists in the image or
            if a column triggered the _update attribute to flip. If
            either condition is met, set schema _update attribute to
            true and write that file and write the contents of the 
            rendered template to that file. See jinja2 src.TEMPLATES.\
            data.change or jinja2 docs for more information. If it does 
            exist or we're not to update, do nothing.

        returns - None
        """
        if not exists(self._dir) or True in [col._update for col in self._columns]:
            with open(self._dir, "w+") as f:
                template = self._schema._database._env.get_template('template.data')
                rendered = template.render(TABLE=self)
                f.write(rendered)

    def _read_data(self):
        """
        _read_data(self):

        function: if the expected table file, self._dir, exists, open that
            file in read only and extract it's text line by line. Otherwise,
            we return the empty list.

        returns - list
        """
        if exists(self._dir):
            with open(self._dir) as f:
                return f.readlines()
        else:
            return [] 

# COLUMN.py
        self._update = False
        self.check_existance()

    def check_existance(self):
        """
        check_existance(self)

        function: If table needs to be updated or column name is not
            in the existing database image, update the table and column
            _update parameter. 

        returns - None
        """
        if f"{self._name}\n" not in self._table.read_data:
            self._table._schema._database._update = True
            self._table._schema._update = True
            self._table._update = True
            self._update = True
            print(self)


