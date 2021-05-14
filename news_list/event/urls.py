from . import views
from django.urls import path, re_path


urlpatterns = [
    path('', views.index, name='home'),
    path('post/<slug:event_slug>/', views.event, name='event'),
    path('cat/<slug:cat_slug>/', views.category_list, name='cat'),
    #path('search/<str:search>', views, name='search'),


    re_path(r'^archive/(?P<year>[0-9]{4})/', views.archive)

]


