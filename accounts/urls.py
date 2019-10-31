from . import views
from django.urls import path,include

app_name = ''

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('activate/<uidb64>/<token>',views.activate, name='activate'),
    path('',include('django.contrib.auth.urls')),
]