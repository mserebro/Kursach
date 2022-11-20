

from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    if request.GET:
        print(request.GET)
    
    return HttpResponse("<h1>Страница библиографических ссылок</h1>")
    
    
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
    
