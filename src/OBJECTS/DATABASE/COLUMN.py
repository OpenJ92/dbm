class COLUMN(object):
    def __init__(self, TABLE, name, data, ACTION = [], POST_ACTION = []):
        """
        __init__(self, TABLE, name, data):
            TABLE::src.OBJECTS.TABLE.TABLE - table object defined
            ---@ scd/src/OBJECTS/TABLE
            name::string 
            data::pandas.DataFrame - Filtered data queried from src.CONNECT object

        attributes:
            _update::bool - Update flag
            _table::src.OBJECTS.TABLE.TABLE
            _name::string - Table name
            _data::dict - key : value pairs from the extracted row from 
            --- original query

        function: Attribute nessesary state to src.OBJECT.TABLE.TABLE
            object, check the existance of such a table in currently stored
            images, and update coresponding tables _update attribute if it 
            does not exist.
        """
        self._parent = TABLE
        self._name = name
        self._ACTION = ACTION
        self._POST_ACTION = POST_ACTION
        self._actions = {action.__name__ : action(self).O().__act__() for action in ACTION}
        self._data = self.reform_data(data)
        self._post_actions = {action.__name__ : action(self).O().__act__() for action in POST_ACTION}

    def __getitem__(self, item):
        """
        __getitem__(self, item)
        item::int

        function: Afford src.OBJECT.DATABASE.DATABASE itterable
            behaviors for use in loops.

        returns - src.OBJECT.SCHEMA.SCHEMA
        """
        return self._data[item]

    def reform_data(self, data):
        """
        reform_data(self, data):
            data::pandas.DataFrame - Row of dataframe coresponding to column name

        function: Form pandas.DataFrame object which is better suited for use in 
            jinja2 templates

        returns - dict
        """
        return {key : value for key, value in data.iloc[0].items()}
