from django.shortcuts import render
from django.core.mail import send_mail, mail_admins, BadHeaderError


def say_hello(request):
    try:
        send_mail("subject", "messages", "info@mat.com", ["some@ex.com"])
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Mosh'})
