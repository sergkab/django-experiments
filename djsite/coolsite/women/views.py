from django.shortcuts import render

from django.shortcuts import render, redirect

from .models import *


from django.http import HttpResponse

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})

def categories(request, catid):
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")



