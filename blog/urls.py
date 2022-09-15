from . import views
from django.urls import path

urlpatterns = [
    # Need to come back here and check
    path('', views.PostList.as_view(), name='blog'),
    path('add/', views.add_post, name='add_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]