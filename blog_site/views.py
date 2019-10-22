from django.http import HttpResponse
from django.shortcuts import render
from posts.models import Post

def index(request):
    posts = Post.objects.all()
    return render(request,'welcome.html',{'posts':posts})