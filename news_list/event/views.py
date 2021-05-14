from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from event.models import *

categorys= Category.objects.all()
posts = Event.objects.order_by('-pub_date').all()

def index(request):
    #if request.GET:
    #    print(request.GET)
    title ='Главная страница'
    return render(request, 'event/base.html',{'category':categorys, 'posts':posts, 'title':title})


def event(request, event_slug):
    post=Event.objects.get(slug=event_slug)
    title=post.title
    return render(request, 'event/event.html',{'category':categorys,'post':post, 'title':title})


def category_list(request, cat_slug):

    posts= Event.objects.filter(category=Category.objects.get(slug=cat_slug))
    title = posts.first().category.title
    category_selected = cat_slug
    return render(request, 'event/base.html', {'category': categorys, 'posts': posts, 'title':title})

def search(request, search_slug):
    pass


def archive(request, year):
    year = int(year)
    if year>2020:
        #raise Http404
        #return HttpResponseNotFound('<h1>Страница не найдена</h1>')
        return redirect('home', permanent=True)
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')