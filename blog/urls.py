from . import views
from django.urls import path

urlpatterns = [
    # Need to come back here and check
    path('', views.PostList.as_view(), name='journal'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]