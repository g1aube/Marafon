from celery import Celery
import time

app = Celery(broker='redis://127.0.0.1:6379/',
             backend='redis://127.0.0.1:6379/2')

@app.task
def func(x):
    time.sleep(1)
    return x