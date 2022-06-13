from django.core.mail import EmailMessage, BadHeaderError
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage
from .tasks import notify_customers

def say_hello(request):
    # try:
    #    message = BaseEmailMessage(
    #        template_name='emails/hello.html',
    #        context={'name': 'Mosh'}
    #    )
    #    message.send(['john@moshbuy.com'])
    # except BadHeaderError:
    #     pass
    notify_customers.delay("hello in view")
    return render(request, 'hello.html', {'name': 'Mosh'})
