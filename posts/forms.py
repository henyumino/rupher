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
            'desc' : SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(NewPostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'placeholder' : 'title'
        })
        self.fields['slug'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'slug'
        })
        self.fields['thumbnail'].widget.attrs.update({
            'class': 'custom-file-input',
            'id'   : 'customFile',
        })