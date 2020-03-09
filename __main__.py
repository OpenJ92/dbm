from src.CONNECT import CONNECT
from src.OBJECTS.DATABASE.DATABASE import DATABASE

from src.OBJECTS.ACTIONS.LOCATE.context import LOCATE
from src.OBJECTS.ACTIONS.POLICY.context import POLICY
from src.OBJECTS.ACTIONS.DBT.context import DBT
from src.OBJECTS.UNARY.CHANGE_REPORT import CHANGE_REPORT

if __name__ == '__main__':
    with CONNECT('RAW') as raw:
        data = DATABASE(raw, ACTION = [LOCATE, POLICY], POST_ACTION = [DBT])
        # CHANGE_REPORT(data)

# access to global macros https://stackoverflow.com/questions/5034437/accessing-global-attributes-from-inside-a-macro-in-jinja2
