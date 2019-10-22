from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def index(request):
    # posts = Post.objects.all()
    # output= ', '.join([str(post) for post in posts])
    # return HttpResponse(output)
    return render(request,'posts/index.html')
