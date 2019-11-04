from . import views
from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.conf.urls import handler404, handler500
from django.conf.urls.static import static

app_name = 'posts'

urlpatterns = [
    path('', views.index,name='index'),
    path('<slug:slug>', views.single, name='single'),
    path('comment/<int:id>', views.comment,name='comment'),
    path('comment-edit/<int:id>', views.comment_edit,name='comment-edit'),
    path('new/',views.post_new, name='post-new'),
]

hander404 = 'views.handler404'

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)