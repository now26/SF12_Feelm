from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User

from rest_framework_simplejwt.tokens import RefreshToken


# 사용자 정보
class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'nickname',
            'profile_image',
            'gender',
            'age',
        )

# 회원가입
class SignupSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=128, min_length=8, write_only=True)
    password2 = serializers.CharField(max_length=128, min_length=8, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)
    
    class Meta:
        model = User
        fields = (
            'username',
            'nickname',
            'profile_image',
            'gender',
            'age',
            'token',
            'password1',
            'password2',
        )
        read_only_fields = ('token',)
        
    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError("Passwords must match.")
        return attrs
    
    def create(self, validated_data):
        # password2는 validated_data에서 제거
        validated_data.pop('password2')

        # password1과 password2를 validated_data에서 제거하고 실제 User 모델에 저장
        password = validated_data.pop('password1')
        user = User.objects.create_user(password=password, **validated_data)
        return user
    
# 로그인
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200, write_only=True)
    password = serializers.CharField(max_length=200, write_only=True)

    token = serializers.CharField(max_length=255, read_only=True)
    
    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)
        # print(data)
        if username is None:
            raise serializers.ValidationError('Username is required to login.')
        
        if password is None:
            raise serializers.ValidationError('Password is required to login.')
        
        user = authenticate(username=username, password=password)
        
        if user is None:
            raise serializers.ValidationError('A user with this ID and password was not found.')
        
        if not user.is_active:
            raise serializers.ValidationError('This user has been deactivated.')
        
        user.save()

        # 토큰 갱신 방식 (Refresh Token + Access Token)
        # JWT 토큰 생성
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        return {
            'username': user.username, 'nickname': user.nickname, 'access_token': access_token, 'refresh_token': refresh_token
        }