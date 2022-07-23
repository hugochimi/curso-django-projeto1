from django.http import HttpResponse

# from django.shortcuts import render

# Create your views here.


def home(request):
    # HTTP Response
    return HttpResponse('HOME')


def contato(request):
    # HTTP Response
    return HttpResponse('Contato')


def sobre(request):
    # HTTP Response
    return HttpResponse('Sobre')
