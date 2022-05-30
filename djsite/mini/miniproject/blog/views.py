from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h2>Hello, Django 30 05 2022!</h2>')

def test(request):
    return HttpResponse('<h2>Hello, it is test 30 05 2022!</h2>')



