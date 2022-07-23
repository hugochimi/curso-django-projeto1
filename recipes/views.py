# from operator import imod

from django.shortcuts import render

# from django.shortcuts import render

# Create your views here.


def home(request):
    # HTTP Response
    return render(request, 'recipes/home.html', context={
        'name': 'Huguera',
    })
