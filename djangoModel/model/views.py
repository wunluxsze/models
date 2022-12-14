
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from model.forms import PostForm
from model.models import Post


def add_new(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        isPublish = request.POST.get('isPublish')
        date = request.POST.get('date')
        if isPublish:
            post = Post.objects.create(title=title, content=content, date=date)
            post.save()
            return redirect('all')
        else:
            return HttpResponse('<h2>Post not published</h2>')
    else:
        postform = PostForm()
        return render(request, 'posts.html', {'form': postform})


def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'index.html', context={'posts': posts})