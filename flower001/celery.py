from __future__ import absolute_import, unicode_literals
import os
from datetime import timedelta

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flower001.settings')

app = Celery('flower001')
app.conf.enable_utc = False

app.conf.update(timezone='Asia/Kolkata')
app.config_from_object(settings, namespace='CELERY')
app.conf.beat_schedule = {
    'Send_mail_to_Client': {
        'task': 'app001.tasks.check_sum',
        'schedule': timedelta(seconds=30),  # every 5 seconds it will be called
        #       # 'args': (2,) you can pass arguments also if rquired
    }
}
app.autodiscover_tasks()

# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {"emai"}')
