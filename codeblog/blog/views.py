from django.shortcuts import render, redirect, get_object_or_404
from . models import Category, Post
from . forms import CommentForm
from core.models import Setting
from django.db.models import Q

# Create your views here.



def detail_view(request, slug):
    
    settings = Setting.objects.all()[0]
    post = get_object_or_404(Post, slug=slug)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()

    context = {'post': post, 'form': form, 'settings': settings}
    return render(request, 'blog/detail.html', context)


def category_view(request, slug):
    settings = Setting.objects.all()[0]
    title = "Post Category | Codeblog"
    
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status = Post.ACTIVE) #type: ignore
    
    context = {'category': category, 'posts': posts, 'page_title': title, 'settings': settings}
    return render(request, 'blog/categories.html', context)


def search_view(request):
    
    query = request.GET.get('search', ' ')
    posts = Post.objects.filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query))
    settings = Setting.objects.all()[0]
    category = []
    context = {}
    title = "Search | Codeblog"
    
    context = {'category': category, 
               'posts': posts, 
               'page_title': title, 
               'settings': settings, 
               'query': query}
    return render(request, 'blog/search.html', context)
