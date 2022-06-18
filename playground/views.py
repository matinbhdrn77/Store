from django.core.mail import EmailMessage, BadHeaderError
from django.shortcuts import render
import requests
from templated_mail.mail import BaseEmailMessage
from django.core.cache import cache
from rest_framework.views import APIView
from .tasks import notify_customers


class HelloView(APIView):
    def get(self, request):
        response = requests.get('https://httpbin.org/delay/10')
        data = response.json()
        return render(request, 'hello.html', {'name': 'mat'})


def say_hello(request):
    key = 'httpbin_result'
    if cache.get(key) is None:
        print('caching...')
        response = requests.get('https://httpbin.org/delay/10')
        data = response.json()
        cache.set(key, data, 2)
    return render(request, 'hello.html', {'name': cache.get(key)})


def say_hello(request):
    try:
        message = BaseEmailMessage(
            template_name='emails/hello.html',
            context={'name': 'Mosh'}
        )
        message.send(['john@moshbuy.com'])
    except BadHeaderError:
        pass


def say_hello(request):
    notify_customers.delay("hello in view")
    return render(request, 'hello.html', {'name': 'Mosh'})
