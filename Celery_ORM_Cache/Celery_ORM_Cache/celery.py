import os

from celery import Celery
# for schedule
from datetime import timedelta
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Celery_ORM_Cache.settings')

app = Celery('Celery_ORM_Cache')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

# celery_beat # run in background with specitic time,date and as per user requirenments
# using timedelta function
'''app.conf.beat_schedule = {
    'every-40-seconds':{
        'task':'myapp.tasks.clear_session_cache',
        'schedule':timedelta(seconds=40), # for every 40 seconds its called
        'args':('123123',)
    }
}'''

''' ex.1'''
# using crontab - best approach
app.conf.beat_schedule = {
    'every-40-seconds':{
        'task':'myapp.tasks.clear_session_cache',
        'schedule':crontab(minute='*/1'), # for every 1 minutes  its called
        'args':('123123',)
    }
}

''' ex.2'''
# https://docs.celeryq.dev/en/latest/userguide/periodic-tasks.html
'''app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'add-every-monday-morning': {
        'task': 'myapp.tasks.clear_session_cache',
        'schedule': crontab(hour=7, minute=30, day_of_week=1),
        'args': (16, 16),
    },
}'''


