from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('posts/',include('posts.urls')),
    path('', views.index),
    path('admin/', admin.site.urls),
]
