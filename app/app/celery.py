from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
# from rest_framework.authtoken.models import Token
# import requests

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

app = Celery('app')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

app.conf.beat_schedule = {
    "email-total-docs++": {
        "task": "api.tasks.auto_increment_task",
        "schedule": 10.0
    },
    "count-total-docs": {
        "task": "api.tasks.print_total_file",
        "schedule": 5.0
    },
}