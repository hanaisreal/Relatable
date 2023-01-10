from rest_framework import serializers
from .models import User
from rest_framework_jwt.settings import api_settings
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
    


#계정 생성 직후에 사용자에게 토큰을 반환하기 위해 수동으로 토큰을 생성하는 메소드
class UserSerializerWithToken(serializers.ModelSerializer):
    
    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
    class Meta:
        model = User
        fields = (
            "username",
            "nickname",
            "intro"
        )