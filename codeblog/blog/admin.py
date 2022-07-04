from typing import Dict, Sequence
from django.contrib import admin
from . models import Category, Post, Comment

# Register your models here.

class CommentItemInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ['post']

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'intro', 'body']
    list_display = ['title', 'slug', 'category', 'created_at', 'status']
    list_filter  = ['category', 'created_at', 'status']
    inlines = [CommentItemInline]
    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    search_fields = ['fullname', 'body']
    
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title', 'slug']
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)