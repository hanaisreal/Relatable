from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  #works
    path('login/', LoginView.as_view(), name='login'),  #works
    path('user/', UserView.as_view(), name='get user info'),
    path('logout/', LogoutView.as_view(), name='logout'),
]