from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("YHWH")

def greet(request, name):
    return HttpResponse(f'Hey, {name}!')