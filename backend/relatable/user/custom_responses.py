from user.serializers import UserInfoSerializer

def my_jwt_response_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserInfoSerializer(user, context={'request': request}).data
    }