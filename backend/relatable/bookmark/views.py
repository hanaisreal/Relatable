from django.shortcuts import render
from bookmark.models import Bookmark
from post.serializers import PostListSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import permissions, authentication
from django.http import HttpResponse, JsonResponse
# Create your views here.

@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def bookmarked_posts_by_user(request):
    if not request.user.is_authenticated:
        return HttpResponse(status=401)
    user = request.user.id
    user_bookmark = Bookmark.objects.filter(user=user)
    posts = [
        bookmark.post for bookmark in user_bookmark]

    data = PostListSerializer(posts, many=True, context={
        'user': request.user}).data
    return JsonResponse({"posts": data, "count": len(posts)}, safe=False)

