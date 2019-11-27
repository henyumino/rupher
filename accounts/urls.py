from . import views
from django.urls import path,include
from accounts.forms import CustomLoginForm
from django.contrib.auth import views as auth_views 

app_name = ''

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html', authentication_form=CustomLoginForm), name='login'),
    path('activate/<uidb64>/<token>',views.activate, name='activate'),
    path('',include('django.contrib.auth.urls')),
    path('settings/',views.edit_user,name='edit-user'),
]