from django import forms
from django.forms import ModelForm
from .models import Post,Comment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class NewPostForm(ModelForm):
    title = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class': 'form-control'}))
    slug = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class': 'form-control'}))
    desc = forms.CharField(widget=SummernoteWidget())
    # thumbnail = forms.FileField(forms.FileField(attrs={'class':'form-control'}))  

    class Meta:
        model = Post
        fields = ('title','slug','desc','status')
        widgets = {
            'desc' : SummernoteWidget(),
        }
