from rest_framework import serializers
from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "password",
            "nickname",
            "intro",
            "profile_img",
            "logged_in",
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):  #비밀번호 암호화
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
