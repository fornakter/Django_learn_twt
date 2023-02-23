from django.shortcuts import render
from django.http import HttpResponse

def index(response):
    return HttpResponse('Kurwa!')

def v1(response):
    return HttpResponse('Kurwa dwa!')