from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from .models import Post

def handler404(request):
    return render(request, '404.html', status=404)

def index(request):
    posts = Post.objects.all()
    return render(request,'posts/index.html',{'posts':posts})

def single(request, slug):
    post = get_object_or_404(Post,slug = slug)
    return render(request,'posts/single.html',{'post':post})
