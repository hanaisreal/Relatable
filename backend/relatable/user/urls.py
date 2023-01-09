from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_id>/', views.get_user, name='get user'), #ok
    path('signup/', views.signup, name='sign up'),  #ok
    path('login/', views.login, name='log in'),  #no
    path('logout/', views.logout, name='log out'),
    path('me/', views.my_info, name='my info'),
    #path('token/', views.token, name='token'),
]