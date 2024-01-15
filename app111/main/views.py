from django.shortcuts import render
from django.http import HttpResponse


def index(request) -> HttpResponse:
    context = {'title': 'Home',
               'content': 'главная страница магазина '}
    return render(request, 'main/index.html',context)


def about(request) -> HttpResponse:
    return HttpResponse('about page')
