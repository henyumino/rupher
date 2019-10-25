from . import views
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('posts/',include('posts.urls',namespace='posts')),
    path('', views.index,name='home'),
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls', namespace='accounts'))

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
