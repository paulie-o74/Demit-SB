from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('collabs/', views.collabs, name="collabs"),
    path('murals/', views.murals, name="murals"),
    path('paintings/', views.paintings, name="paintings"),
    path('contact/', views.contact, name="contact"),
]