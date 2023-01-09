from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import permissions, authentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.contrib.auth import authenticate, login, logout
from .serializers import UserInfoSerializer, UserBasicInfoSerializer
import json
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.

@api_view(['GET'])  #Takes a list of HTTP methods that views should respond to 
@ensure_csrf_cookie
def token(request):
    if request.method == 'GET':
        return HttpResponse(status = 204)

@api_view(['POST'])        
def signup(request): #OK
    if request.method == 'POST':

        try:
            request_data = request.data.copy()
            username = request_data['username']
            password = request_data['password']
            intro = request_data['intro']
            nickname = request_data['nickname']

            user = User.objects.create_user(
                username=username, password=password, intro=intro, nickname=nickname 
            )
            Token.objects.create(user = user)  #token key should be included in the authorization http header

            return HttpResponse(status = 201)
            
        except Exception as e:
            print(e)
            return HttpResponse(status = 400)

@api_view(['POST'])
def login(request):  #no 
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
def logout(request):
    if request.method == 'POST':
        user = request.user
        if user.is_authenticated:
            user.logged_in = False
            user.save()
            logout(request)
            return HttpResponse(status=200)



@api_view(['GET'])
def get_user(request, user_id):  #OK
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return HttpResponseNotFound(f"No user matches id={user_id}")

    data = UserBasicInfoSerializer(user).data
    return JsonResponse(data, safe=False)

 
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([authentication.TokenAuthentication])  #토큰을 확인. 토큰이 이상이 있으면 에러를 JSON 형식으로 반환
@permission_classes([permissions.IsAuthenticated])     #로그인 했는지 여부만 체크    
def my_info(request):
    if request.method == 'GET':
        user = request.user
        if user.is_authenticated:
            data = UserInfoSerializer(user).data
            return JsonResponse(data, safe=False)
    elif request.method == 'PUT':
        user = request.user
        req_data = json.loads(request.body.decode())

        if check_password(req_data['org_password'], user.password):
            password = req_data['password']
            user.set_password(password)
            user.save()

            login(request, user)

            data = UserInfoSerializer(user).data

            return JsonResponse(data, safe=False)
        else:
            return HttpResponse(status = 400)
    
    elif request.method == 'DELETE':
        user = request.user

        if user.is_authenticated:
            user.delete()
            return HttpResponse(status=200)