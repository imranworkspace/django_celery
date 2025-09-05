from celery import shared_task
from time import sleep

@shared_task(name="subtraction_task")
def sub(x,y):
    sleep(10)
    return x-y

@shared_task(name="addition_task")
def add(x,y):
    sleep(20) # holding for 20 seconds
    return x+y
