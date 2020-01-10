from src.CONNECT import CONNECT
from src.OBJECTS.DATABASE import DATABASE

if __name__ == '__main__':
    with CONNECT('RAW') as raw:
        data_raw = DATABASE(raw)
        # send email with policy template to donn.
        # await
