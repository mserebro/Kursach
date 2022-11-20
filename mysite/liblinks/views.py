
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound


field = ["Статья из сборника","Фамилии и инициалы авторов (через запятую)","Заголовок статьи из сборника","Название сборника","Город, в котором издан сборник","Издательство","Год издания","Страницы"]

def index(request):
    if request.GET:
        print(request.GET)
    
    return render(request, 'liblinks/index.html',{'field': field, 'title': 'Оформление библиографических ссылок'})
    
    return HttpResponse("<h1>Страница библиографических ссылок</h1>")
    
    
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
    
