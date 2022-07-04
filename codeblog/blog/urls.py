from django.urls import path
from . import views

urlpatterns = [
    path('find/', views.search_view, name="search"),
    path('category/<slug:slug>/', views.category_view, name="post_category"),
    path('<slug:slug>/', views.detail_view, name="post_detail"),
    
]