from try_celery.celery import app as celery_app

__all__ = ('celery_app',)

# if not working try this:
# from __future__ import absolute_import, unicode_literals
# from main.celery import app as celery_app
# __all__ = ('celery_app',)
