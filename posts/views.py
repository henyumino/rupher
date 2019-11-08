from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post,Comment
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string
from .forms import NewPostForm

def handler404(request):
    return render(request, '404.html', status=404)

def index(request):
    posts = Post.objects.order_by('-created_at')
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

        post.comment_set.create(desc=newDesc,user=request.user)
        return HttpResponseRedirect('/posts/%s'%post.slug) 

def comment_edit(request,id):
    comment = get_object_or_404(Comment, pk=id)

    if request.user.id != comment.user.id:
        return render(request, '404.html')

    if request.method == 'POST':
        newDesc = request.POST['desc']
        Comment.objects.filter(pk=id).update(desc=newDesc)
        return HttpResponseRedirect('/posts')
    
    return render(request, 'posts/comment_edit.html',{'comment':comment})

def post_new(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = request.user.id
            post.save()
            return HttpResponseRedirect('/posts')
    else:
        form = NewPostForm()

    return render(request, 'posts/new.html',{'form':form})

def post_edit(request,slug):
    post = get_object_or_404(Post, slug=slug)
    form = NewPostForm(instance=post)

    active_user = str(request.user.id)

    if active_user != post.user_id:
        return render(request, '404.html')

    if request.method == 'POST':
        form = NewPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dashboard/')

    # tinggal buat edit post saja

    return render(request, 'posts/edit_post.html',{'form':form})

   