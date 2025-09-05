from celery import shared_task
from time import sleep

@shared_task
def mul(x,y):
    sleep(10) # holding for 20 seconds
    return x*y
