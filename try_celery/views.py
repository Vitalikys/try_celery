# from .service import send
from django.shortcuts import render
from django.views.generic import CreateView, ListView

from .forms import ContactForm
from .models import Contact
from .tasks import *
from try_celery.service import send


class Home(ListView):
    model = Contact
    template_name = 'try_celery/base.html'


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        # send(form.instance.email)   # use this for simply form
        send_spam_email.delay(form.instance.email)  # delay - not waiting
        return super().form_valid(form)


'''
Django School /celery django примеры #2 time 30:00
 celery -A send_email worker -l info
'''
