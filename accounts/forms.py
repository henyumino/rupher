from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm,PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms.widgets import PasswordInput, TextInput

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Email'}),max_length=200,help_text='Required')
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Username'}),max_length=200,help_text='Required')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Password'}),max_length=200,help_text='Required')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Confirm Password'}),max_length=200,help_text='Required')

    class Meta:
        model = User
        fields = ('username','email','password1','password2')


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Username'}),max_length=200,help_text='Required')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Password'}),max_length=200,help_text='Required')

    class Meta:
        model = User
        fields = '__all__'

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Old Password'}),max_length=200,help_text='Required')
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'New Password'}),max_length=200,help_text='Required')
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Confirm New Password'}),max_length=200,help_text='Required')
    
    class Meta:
        model = User
        field = '__all__'

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Email'}),max_length=200,help_text='Required')
    
    class Meta:
        model = User
        field = '__all__'

class CustomSetPassword(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'New Password'}),max_length=200,help_text='Required')
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Confirm New Password'}),max_length=200,help_text='Required')

    class Meta:
        model = User
        field = '__all__'