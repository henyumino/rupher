from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post,Comment

def handler404(request):
    return render(request, '404.html', status=404)

def index(request):
    posts = Post.objects.all()
    return render(request,'posts/index.html',{'posts':posts})

def single(request, slug):
    post = get_object_or_404(Post,slug = slug)
    return render(request,'posts/single.html',{'post':post})

def comment(request,id):
    post = get_object_or_404(Post, pk=id)

    if request.method == 'POST':
        newDesc = request.POST['desc']

        if len(newDesc) < 10:
            return render(request, 'posts/single.html',{
                                'post':post,
                                'errors':'minimal 10 karakter'
                                })

        post.comment_set.create(desc=newDesc,user_id='1')
        return HttpResponseRedirect('/posts/%s'%post.slug) 

def comment_edit(request,id):
    comment = get_object_or_404(Comment, pk=id)

    if request.method == 'POST':
        newDesc = request.POST['desc']
        Comment.objects.filter(pk=id).update(desc=newDesc)
        return HttpResponseRedirect('/posts')
    
    return render(request, 'posts/comment_edit.html',{'comment':comment})