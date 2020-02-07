from src.CONNECT import CONNECT
from src.OBJECTS.DATABASE.DATABASE import DATABASE

from src.OBJECTS.ACTIONS.CHECK.context import CHECK
from src.OBJECTS.UNARY.CHANGE_REPORT import CHANGE_REPORT
from src.OBJECTS.UNARY.DBT import DBT

if __name__ == '__main__':
    with CONNECT('RAW') as raw:
        data = DATABASE(raw, ACTION = [CHECK])
        DBT(data)
