from django import forms
from django.forms import ModelForm
from .models import Post,Comment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class NewPostForm(ModelForm):
    title = forms.CharField(max_length=255)
    slug = forms.CharField(max_length=255)
    desc = forms.CharField(widget=SummernoteWidget())  

    class Meta:
        model = Post
        fields = ('title','slug','thumbnail','desc','status')
        widgets = {
            'desc' : SummernoteWidget()
        }
