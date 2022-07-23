from operator import imod

from django.http import HttpResponse
from django.shortcuts import render

# from django.shortcuts import render

# Create your views here.


def home(request):
    # HTTP Response
    return render(request, 'recipes/home.html', context={
        'name': 'Huguera',
    })


def contato(request):
    # HTTP Response
    return render(request, 'temp.html')


def sobre(request):
    # HTTP Response
    return HttpResponse('Sobre')
