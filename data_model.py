from src.CONNECT import CONNECT
from src.OBJECTS.DATABASE import DATABASE

if __name__ == '__main__':
    with CONNECT('raw') as raw, CONNECT('analytics') as analytics:
        data_raw = DATABASE(raw)
