from . import views
from django.urls import path,include

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('',include('django.contrib.auth.urls')),
]