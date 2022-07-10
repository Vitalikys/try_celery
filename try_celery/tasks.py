from celery import shared_task
from django.core.mail import send_mail

from try_celery.celery import app
# from main.celery import app
from .models import Contact
from .service import send


@app.task
def add(x, y):
    return x + y


@app.task
def send_spam_email(user_email):
    send(user_email)


@app.task
def send_email_5_min_beat():
    for contact in Contact.objects.all():
        send_mail(  # standart funct from django.core.mail import ...
            'You are subscribed for SPAM',
            'You will got a lot of spam every 5 minute. @app.task $send_email_5_min_beat ',
            'gonevich91@ukr.net',  # пошта з якої відправляється
            [contact.email],  # пошта призначення
            fail_silently=False,
        )


@app.task(bind=True, default_retry_delay=7 * 60)
def my_task_retry(self, x, y):
    try:
        return x + y
    except Exception as exc:
        raise self.retry(exc=exc, coundown=60)

@shared_task()
def hello(st):
    return (st+'!! ')*3

'''
https://django.fun/docs/celery/ru/5.1/getting-started/first-steps-with-celery/#application
$  celery -A try_celery.tasks worker -l info     ERROR
$ celery -A try_celery worker --loglevel=INFO  ОК  
$ celery -A try_celery beat -l info         ok запуск beat

 $ my_task_retry.apply_async((55,44), countdown=60)
'''
