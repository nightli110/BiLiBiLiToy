import datetime
from schedule import run_pending
import time
from core.process import *



if __name__ == "__main__":
    while True:
        try:
            run_pending()
            time.sleep(1)
        except Exception as e:
            print(e)