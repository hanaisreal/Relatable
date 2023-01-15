from rest_framework import serializers
from bookmark.models import Bookmark
from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source="user.username")
    title = serializers.CharField(required=True)
    content = serializers.CharField(required=True)
    created_at = serializers.DateTimeField(required=True)
    updated_at = serializers.DateTimeField(required=True)
    like = serializers.BooleanField()
    public = serializers.BooleanField()
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            "id",
            "username",
            "title",
            "content",
            "created_at",
            "updated_at",
            "like",
            "public",
            "tags"
        )


    def get_tags(self, post):
        tags = post.tags.all()
        result = []
        for tag in tags:
            result.append(tag.name)
        return result

    # def get_category_tags(self, obj):
    #     return [t.category_tags.content for t in obj.category_tags.all()]

    # def get_is_bookmarked(self, obj):
    #     try:
    #         user = self.context['user']
    #         if user.is_authenticated:
    #             try:
    #                 Bookmark.objects.get(user=user.id, post=obj.id)
    #             except Bookmark.DoesNotExist:
    #                 return False
    #             return True
    #         return False
    #     except KeyError:
    #         return False