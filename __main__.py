from src.CONNECT import CONNECT
from src.OBJECTS.DATABASE.DATABASE import DATABASE

if __name__ == '__main__':
    with CONNECT('RAW') as raw:
        data_raw = DATABASE(raw)
