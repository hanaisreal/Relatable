from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = { 
            'password': {'write_only': True}  #password not returned 
        }


    def create(self, validated_data):  #비밀번호 암호화
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)   #hash password 
        instance.save()
        return instance