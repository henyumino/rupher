from . import views
from django.urls import path,include
from accounts.forms import CustomLoginForm, CustomPasswordChangeForm, CustomPasswordResetForm, CustomSetPassword
from django.contrib.auth import views as auth_views 

app_name = ''

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True,template_name='registration/login.html', authentication_form=CustomLoginForm), name='login'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html',form_class=CustomPasswordChangeForm), name='password_change'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html',form_class=CustomPasswordResetForm), name='password_reset'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html',form_class=CustomSetPassword), name='password_reset_confirm'),
    path('activate/<uidb64>/<token>',views.activate, name='activate'),
    path('',include('django.contrib.auth.urls')),
    path('settings/',views.edit_user,name='edit-user'),
]