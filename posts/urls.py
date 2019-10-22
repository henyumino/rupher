from . import views
from django.contrib import admin
from django.urls import path
from django.conf.urls import handler404, handler500

app_name = 'posts'

urlpatterns = [
    path('', views.index,name='index'),
    path('<slug:slug>', views.single, name='single'),
]

hander404 = 'views.handler404'