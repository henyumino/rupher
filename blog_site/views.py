from django.http import HttpResponse
from django.shortcuts import render
from posts.models import Post
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    posts = Post.objects.order_by('-created_at')
    paginator = Paginator(posts,9)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request,'welcome.html',{'posts':posts,'domain':settings.CURRENT_DOMAIN})

def dashboard(request):
    posts = Post.objects.filter(user_id=request.user.id).order_by('-created_at')
    post_count = posts.count()
    post_pub = Post.objects.filter(user_id=request.user.id,status='PUBLISHED')
    post_pub = post_pub.count()
    return render(request,'dashboard.html',{'posts':posts,'domain':settings.CURRENT_DOMAIN,'post_count':post_count,'post_pub':post_pub})

