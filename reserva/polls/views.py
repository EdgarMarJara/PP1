from django.shortcuts import render 

from django.http import HttpResponse


def index(request):
    return HttpResponse("Buenas este es el parcial de Edgar Martinez de PP1")

# Create your views here.
