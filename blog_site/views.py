from django.http import HttpResponse
from django.shortcuts import render
from posts.models import Post

def index(request):
    posts = Post.objects.order_by('-created_at')
    return render(request,'welcome.html',{'posts':posts})

def dashboard(request):
    posts = Post.objects.filter(user_id=request.user.id).order_by('-created_at')
    return render(request,'dashboard.html',{'posts':posts})

