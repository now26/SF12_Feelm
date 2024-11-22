from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User, Diary
from movies.models import Movie, Review

from rest_framework_simplejwt.tokens import RefreshToken


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'id',
            'tmdb_id',
            'title',
            'poster_path',
        )
# 사용자 정보
class UserInfoSerializer(serializers.ModelSerializer):
            
    class ReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = (
                'movie',
                'content',
                'rating',
                'user',
            )
            
    # 유저가 좋아요한 영화
    like_movies = MovieSerializer(many=True, read_only=True, source='like_movies.all')
    # 유저가 북마크한 영화
    bookmark = MovieSerializer(many=True, read_only=True, source='bookmark.all')
    # 유저가 좋아요한 리뷰
    like_reviews = ReviewSerializer(many=True, read_only=True, source='like_reviews.all')
    # 유저가 작성한 리뷰
    reviews = ReviewSerializer(many=True, read_only=True, source='reviews.all')
    
    class Meta:
        model = User
        fields = (
            'username',
            'nickname',
            'profile_image',
            'gender',
            'age',
            'like_movies',
            'bookmark',
            'like_reviews',
            'reviews',
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
        
# 회원 정보 변경
class UserSerializer(serializers.ModelSerializer):
    # 원래 비밀번호 확인할 필드
    password1 = serializers.CharField(max_length=128, min_length=8, write_only=True)
    # 새롭게 정의할 비밀번호와 비밀번호 확인
    password2 = serializers.CharField(max_length=128, min_length=8, write_only=True)
    password3 = serializers.CharField(max_length=128, min_length=8, write_only=True)
    class Meta:
        model = User
        fields = (
            'nickname',
            'profile_image',
            'password1',
            'password2',
            'password3',
            'age',
            'gender',
            # 'token',
        )
        read_only_fields = ('token',)
    
    def update(self, instance, validated_data):
        password1 = validated_data.pop('password1', None)
        password2 = validated_data.pop('password2', None)
        password3 = validated_data.pop('password3', None)
        # if password1 != 유저의 원래 비밀번호:
        #     return serializers.ValidationError('비밀번호가 틀렸습니다.')
        # if password2 != password3:
        #     return serializers.ValidationError('비밀번호가 다릅니다.')
        
        # 현재 비밀번호 확인
        if not instance.check_password(password1):
            raise serializers.ValidationError('비밀번호가 틀렸습니다.')
        
        # 새 비밀번호 일치 확인
        if password2 != password3:
            raise serializers.ValidationError('비밀번호가 일치하지 않습니다.')
        
        # 새 비밀번호가 제공된 경우 업데이트
        if password2:
            instance.set_password(password2)
        
        # 다른 필드 업데이트
        for key, value in validated_data.items():
            setattr(instance, key, value)
        
        instance.save()
        return instance

        
# 일기 
class DiaryListSerializer(serializers.ModelSerializer):
    # movie = MovieSerializer(read_only=True, source='movie.all')
    class Meta:
        model = Diary
        fields = '__all__'
        read_only_fields = ('user',)

class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = '__all__'
        read_only_fields = ('user', 'movie',)