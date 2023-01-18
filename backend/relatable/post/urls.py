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
#     path('post/', views.post, name="post post ")
# ]