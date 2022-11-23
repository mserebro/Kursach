
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound

from .models import *

#field = ["Статья из сборника","Фамилии и инициалы авторов (через запятую)","Заголовок статьи из сборника","Название сборника","Город, в котором издан сборник","Издательство","Год издания","Страницы"]

field = ["Фамилии и инициалы авторов (через запятую)","Заголовок статьи из сборника","Название сборника","Город, в котором издан сборник","Издательство","Год издания","Страницы"]


def index(request):
    posts = Libinks.pbjects.all()
    #if request.GET:
        #print(request.GET)
    context = {
        'posts': posts,
        'field': field,
        'title': 'Оформление библиографических ссылок'
    }

    return render(request, 'liblinks/index.html', context=context)
    
    return HttpResponse("<h1>Страница библиографических ссылок</h1>")

def addliblink(request):
    return HttpResponse("Добавление библиографической ссылки")

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

    
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
    
def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")
