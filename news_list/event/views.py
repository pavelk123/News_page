from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from event.models import *

categorys= Category.objects.all()

def index(request):
    #if request.GET:
    #    print(request.GET)
    return render(request, 'event/base.html',{'category':categorys})

def event(request, event_slug):
    return HttpResponse(f'Страница новости<p>{event_slug}</p>')

def archive(request, year):
    year = int(year)
    if year>2020:
        #raise Http404
        #return HttpResponseNotFound('<h1>Страница не найдена</h1>')
        return redirect('home', permanent=True)
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')