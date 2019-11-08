from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200,help_text='Required')

    class Meta:
        model = User
        fields = ('username','email','password1','password2')


# class UpdateForm(ModelForm):

#     class Meta:
#         model = User 
#         fields = ('image',)
    
