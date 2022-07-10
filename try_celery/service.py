from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'You are subscribed for SPAM',
        'You will got a lot of spam every day',
        'gonevich91@ukr.net',  # пошта з якої відправляється
        [user_email],  # пошта призначення
        fail_silently=False,
    )
