from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('me/', views.bookmarked_posts_by_user, name='retrieve my bookmarked posts'),
    path('posts/<int:post_id>/', views.toggle_bookmark, name='retrieve my bookmarked posts'),
]