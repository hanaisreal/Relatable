from django.shortcuts import render
from json import JSONDecodeError
from django.http import HttpResponseBadRequest, JsonResponse, HttpResponse
from rest_framework import  viewsets, status
from .models import Post, Tag, PostTag
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import permissions, authentication
from rest_framework.decorators import authentication_classes, permission_classes, api_view

from user.authentication import decode_access_token
from rest_framework.authentication import get_authorization_header
from user.models import User
# Create your views here.

class PostViewSet(viewsets.GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated(),)

    def get_permissions(self):
        return self.permission_classes
    
    #GET /api/post/
    def list(self, request):
        
        title = request.GET.get("title", "")
        posts = (
            self.get_queryset().order_by("title")
        )
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
        # user = request.GET.get("user")
        # if user is None:
        #     posts = Post.objects.all()
        # else:
        #     posts = (Post.objects.filter(user = user))
        #     serializer = PostSerializer(posts, many=True)
        # return Response(serializer.data, status=200)


    #POST /api/post/
    def create(self, request):

        auth = get_authorization_header(request).split()

        if auth and len(auth) == 2:   #Bearer and token 
            token = auth[1].decode('utf-8')  #get the second parameter
            id = decode_access_token(token)

            user = User.objects.filter(pk=id).first()

        username = user.get_username
        password = user.get
        request.data._mutable=True
        data = request.data
        tag_data = data.pop("tags", [])
        if not isinstance(tag_data, list):
            return Response(
                {"error": "'tags' should be list"}, status=status.HTTP_400_BAD_REQUEST
            )
        serializer = self.get_serializer(data = data)
        serializer.is_valid(raise_exception=True)
        post = serializer.save()
        post.save()

        for name in tag_data:
            tag, created = Tag.objects.get_or_create(name = name)
            PostTag.objects.create(post=post, tag=tag)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    #GET /api/post/{post_id}/
    def retrieve(self, request, pk=None):
        post = self.get_object()
        return Response(self.get_serializer(post).data, status=status.HTTP_200_OK)
