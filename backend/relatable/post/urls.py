from django import views
from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter
from post.views import PostViewSet

post_app_name = "post"
router = SimpleRouter()
router.register(post_app_name, PostViewSet, basename="post")

urlpatterns = [path("", include(router.urls))]



# urlpatterns = [
#     path('', views.cocktail_list, name='post list'),
#     #path('init/', views.get_init_post, name='get init post'),
#     path('post/', views.post_post, name='post'),
#     path('<int:pk>/', views.retrieve_post, name='retrieve post'),
#     path('<int:pk>/edit/', views.edit_post, name='edit post'),
#     path('<int:pk>/delete/', views.delete_post, name='delete post'),
#     #path('<int:pk>/rate/', views.cocktail_rate_edit, name='cocktail rate edit'),
#     path('me/', views.retrieve_my_posts, name='retrieve my posts')
# ]