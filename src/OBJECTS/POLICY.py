class POLICY(object):
    def __init__(self, obj):
        self._object = obj
        # A Policy is the name of a macro inside dbt folder. 
        # Psudo:
        #   1. Read policy document
        #   2a. Prepare policy text (write policy)
        #   2b. augment object state (execution policy)
        pass

    def materialize(self):
        # construct the strings to be placed into model.sql or
        # schema.yml file. Store this element as an attribute of
        # the policy object
        pass

    def augment(self):
        # adjust the state of the attached object so that we can
        # carry out simple flag checks in the construction of the
        # template 
        pass
