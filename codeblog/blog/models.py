from xmlrpc.client import DateTime
from django.db import models
from django.forms import CharField, DateTimeField, SlugField

# Create your models here.


class Category(models.Model):
    title  = models.CharField(max_length=255)
    slug = models.SlugField()
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.title
    
    

class Post(models.Model):
    category = models.ForeignKey(Category, related_name="posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    
    intro = models.TextField()
    body = models.TextField()
    
    date_added = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Comments"
    
    
    def __str__(self):
        return f"{self.post.title} - {self.fullname}"