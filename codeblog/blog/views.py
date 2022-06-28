from xml.etree.ElementTree import Comment
from django.shortcuts import render, redirect
from . models import Category, Post
from . forms import CommentForm

# Create your views here.

def frontpage_view(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/templates/frontpage.html', context)


def detail_view(request, slug):
    
    post = Post.objects.get(slug=slug)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('detail', slug=post.slug)
    else:
        form = CommentForm()
    
    
    
    context = {'post': post, 'form': form}
    return render(request, 'blog/templates/detail.html', context)


def category_view(request, slug):
    category = Category.objects.get(slug=slug)
    context = {'category': category}
    return render(request, 'blog/templates/categories.html', context)
