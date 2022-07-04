from django.shortcuts import render, redirect
from blog.models import Post
from . forms import ContactForm
from .models import Setting
from django.http import HttpResponse

# Create your views here.

def home_page(request):
    posts = Post.objects.filter(status = Post.ACTIVE)
    settings = Setting.objects.all()[0]
    title = f"Home | {settings.sitename}"
    context = {'page_title':title, 'posts': posts, 'settings': settings}
    return render(request, 'core/homepage.html', context)


def about_page(request):
    
    settings = Setting.objects.all()[0]
    title = "About | Codeblog"
    context = {'page_title':title, 'settings':settings}
    return render(request, 'core/about.html', context)


def foodmenu_page(request):
    settings = Setting.objects.all()[0]
    context = {'settings':settings}
    return render(request, 'core/foodmenu.html', context)


def contact_page(request):
    
    settings = Setting.objects.all()[0]
    title = "Contact Us | Codeblog"

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            return redirect('contactpage')
    
    form = ContactForm()
    context = {'form': form, 'page_title':title, 'settings': settings}
    return render(request, 'core/contact.html', context)


def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/"
    ]
    
    return HttpResponse("\n".join(text), content_type="text/plain")
    
