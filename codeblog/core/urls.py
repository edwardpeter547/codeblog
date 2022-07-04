from django.urls import path
from . import views



urlpatterns = [
    path('', views.home_page, name='homepage'),
    path('robots.txt', views.robots_txt, name='robots_txt' ),
    path('about/', views.about_page, name='aboutpage'),
    path('foodmenu/', views.foodmenu_page, name='foodmenu'),
    path('contact-us/', views.contact_page, name='contactpage'),
]