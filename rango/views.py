from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("khe berga pinshi yango")


def amerika(request):
    return HttpResponse("ke dijistes del amerika wey")