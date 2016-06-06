from django.shortcuts import render
from django.http import HttpResponse


def work(request):
    return HttpResponse("it works")


# Create your views here.
