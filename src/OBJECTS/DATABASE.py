from src.OBJECTS.SCHEMA import SCHEMA

class DATABASE(object):
    def __init__(self, CONNECT):
        self._name = CONNECT.name
        self._data = CONNECT._extract('select * from columns;')
        self._schemas = self.construct_schemas(); del self._data

    def read_policy(self):
        pass

    def construct_schemas(self):
        unique_schema = self._data['TABLE_SCHEMA'].unique()
        return {                                                        
                 schema                                                 
                 :                                                      
                 SCHEMA(                                                
                        self,                                           
                        schema,                                         
                        self._data[
                            self._data['TABLE_SCHEMA'] == schema
                                  ]
                        )                                               
                 for schema in unique_schema                            
               }
