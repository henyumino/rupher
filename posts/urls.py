from . import views
from django.contrib import admin
from django.conf import settings
from django.urls import path,include
from django.conf.urls import handler404, handler500
from django.conf.urls.static import static


app_name = 'posts'

urlpatterns = [
    path('', views.index,name='index'),
    path('<slug:slug>', views.single, name='single'),
    path('comment/<int:id>', views.comment,name='comment'),
    path('comment-edit/<int:id>', views.comment_edit,name='comment-edit'),
    path('<int:id>/edit/', views.post_edit,name='post-edit'),
    path('<int:id>/delete/', views.post_delete,name='post-delete'),
    path('new/',views.post_new, name='post-new'),

    # buat path dasboard!
    
]

hander404 = 'views.handler404'

