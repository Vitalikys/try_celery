''' write here instead of  file tasks.py

'''
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'try_celery.settings')

# app = Celery('try_celery')
app = Celery('try_celery')
# consider with django
app.config_from_object('django.conf:settings', namespace='CELERY')
# add tasks automaticly
app.autodiscover_tasks()
