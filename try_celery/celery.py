''' write here instead of  file tasks.py

'''
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

# app = Celery('try_celery')
app = Celery('try_celery')
# consider with django
app.config_from_object('django.conf:settings', namespace='CELERY')
# add tasks automatically
app.autodiscover_tasks()

''' # приклад для task add(x,y)
# app = Celery('tasks', broker='pyamqp://guest@localhost//')
# щоб не описувати всі настройки так, ми зробили посилання на ....'main.settings.py')
'''

# celery beat TASKS
# https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html
app.conf.beat_schedule = {
    'send_spam_every_5min': {
        'task': 'try_celery.tasks.send_email_5_min_beat',
        'schedule': crontab(minute='*/5'), # періодичність відправлення
    }
}
