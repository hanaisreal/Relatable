from django.http import HttpResponse
from django.shortcuts import render
from .models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import permissions, authentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.contrib.auth import authenticate, login, logout
from .serializers import UserInfoSerializer, UserNameSerializer
# Create your views here.

@api_view(['GET'])  #Takes a list of HTTP methods that views should respond to 
def token(request):
    if request.method == 'GET':
        return HTTPResponse(status = 204)

@api_view(['POST'])        
def signup(request):
    if request.method == 'POST':

        try:
            request_data = request.data.copy()
            username = request_data['username']
            password = request_data['password']

            user = User.objects.create_user(
                username=username, password=password
            )
            Token.objests.create(user = user)  #toen key should be included in the authorization http header

            return HttpResponse(status = 201)
            
        except Exception as e:
            print(e)
            return HttpResponse(status = 400)

@api_view(['POST'])
def signin(request):
    if request.method == 'POST':
        request_data = request.data.copy()
        username = request_data['username']
        password = request_data['password']

        user = authenticate(username = username, password = password)

        if user is not None: # a backend authenticated the credentials
            
            login(request, user)  # login() is given in django, redirect to a success page
            token = Token.objects.get(user = user)
            user.logged_in = True
            user.save()

            user_data = UserInfoSerializer(user).data
            data = {'user_data': user_data, 'token': token.key}
            return Response(data)
        else:
            HttpResponse(status = 401)

 
@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def signout(request):
    if request.method == 'POST':
        user = request.user
        if user.is_authenticated:
            user.logged_in = False
            user.save()
            logout(request)
            return HttpResponse(status=200)


           
