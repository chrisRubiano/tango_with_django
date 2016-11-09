from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import os
# Create your views here.


def index(request):
    context_dict = {'boldmessage': "crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)


def amerika(request):
    return HttpResponse("ke dijistes del amerika wey")