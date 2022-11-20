
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound

from .models import *

#field = ["Статья из сборника","Фамилии и инициалы авторов (через запятую)","Заголовок статьи из сборника","Название сборника","Город, в котором издан сборник","Издательство","Год издания","Страницы"]

field = ["Фамилии и инициалы авторов (через запятую)","Заголовок статьи из сборника","Название сборника","Город, в котором издан сборник","Издательство","Год издания","Страницы"]


def index(request):
    posts = Libinks.pbjects.all()
    #if request.GET:
        #print(request.GET)
    
    return render(request, 'liblinks/index.html',{'posts': posts, 'field': field, 'title': 'Оформление библиографических ссылок'})
    
    return HttpResponse("<h1>Страница библиографических ссылок</h1>")
    
    
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
    
