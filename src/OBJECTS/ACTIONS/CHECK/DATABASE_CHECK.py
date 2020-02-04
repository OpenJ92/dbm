from _CHECK import _CHECK

class DATABASE_CHECK(_CHECK):
    def __init__(self, DATABASE):
        _CHECK.__init__()
        self._exp = f"{self._exp}/{DATABASE._name}"
