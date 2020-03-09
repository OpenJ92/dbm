from src.CONNECT import CONNECT
from src.OBJECTS.DATABASE.DATABASE import DATABASE

from src.OBJECTS.ACTIONS.LOCATE.context import LOCATE
from src.OBJECTS.ACTIONS.POLICY.context import POLICY
from src.OBJECTS.UNARY.CHANGE_REPORT import CHANGE_REPORT
from src.OBJECTS.UNARY.DBT import DBT

if __name__ == '__main__':
    with CONNECT('RAW') as raw:
        data = DATABASE(raw, ACTION = [LOCATE, POLICY])
        # CHANGE_REPORT(data)
        # DBT(data)

# access to global macros https://stackoverflow.com/questions/5034437/accessing-global-attributes-from-inside-a-macro-in-jinja2
