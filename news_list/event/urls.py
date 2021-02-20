from . import views
from django.urls import path, re_path


urlpatterns = [
    path('', views.index, name='home'),
    path('post/<slug:event_slug>/', views.event, name='event'),
    re_path(r'^archive/(?P<year>[0-9]{4})/', views.archive)
]


