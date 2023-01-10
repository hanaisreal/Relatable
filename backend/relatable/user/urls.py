from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_id>/', views.requestUser, name='get user'), #ok
    path('signup/', views.signup, name='sign up'),  #ok
    path('login/', views.signin, name='sign in'),  #no
    path('logout/', views.signout, name='sign out'),
    path('edit/', views.changeSurvey, name='my info'),
    #path('token/', views.token, name='token'),
]