import datetime

from celery_func import func
import time

def main():
    start = datetime.datetime.now()
    a = (func.delay(2))
    b = (func.delay(4))
    c = (func.delay(5))
    print([a.get(), b.get(), c.get()])
    print(datetime.datetime.now() - start)

if __name__ == '__main__':
    main()
