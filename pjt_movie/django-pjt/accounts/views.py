from django.shortcuts import redirect, get_list_or_404, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from rest_framework import status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView

from .models import User, Diary
from .serializers import SignupSerializer, LoginSerializer, UserInfoSerializer, DiarySerializer, DiaryListSerializer, UserSerializer
from .renders import UserJSONRenderer

from movies.models import Movie, Review

import pandas as pd
from movies.serializers import MovieListSerializer
from algo import movie_recommendation_system_combined_rating, movie_recommendation_system_combined_bookmark, load_movie_data

# 회원가입
class SignupAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = SignupSerializer
    # renderer_classes = (UserJSONRenderer,) # pprint와 비슷한 기능
    
    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # 잘 뜨는지 로그인 창으로 리다이렉트 시키기
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
# username 확인 코드 (vue와 연결)
@permission_classes([AllowAny])
@api_view(['GET', 'POST'])
def check_username(request):
    username = request.data.get('username')
    
    if not username:
        return Response({'error': 'Username is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    if User.objects.filter(username=username).exists():
        return Response({'exists': True}, status=status.HTTP_200_OK)
    else:
        return Response({'exists': False}, status=status.HTTP_200_OK)

        
# 로그인
class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    # renderer_classes = (UserJSONRenderer,) # pprint와 비슷한 기능
    serializer_class = LoginSerializer

    def post(self, request):
        # 사용자 정보 가져오기
        username = request.data['username']

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        
        # 로그인 처리
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            login(request, user)

            # JWT 토큰 생성
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)
            # access_token = serializer.validated_data['access_token']
            # refresh_token = serializer.validated_data['refresh_token']
            return Response({
                'access_token': access_token,
                'refresh_token': refresh_token,
            }, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        

# 로그아웃
class LogoutView(APIView):
    # authentication_classes = [SessionAuthentication]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user:
            logout(request)
            return Response({'message':'로그아웃 완료'}, status=status.HTTP_202_ACCEPTED)

# 회원정보 변경
class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    
    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
# 회원탈퇴
# @api_view(['POST'])
# @login_required
# def delete(request):
#     user = request.user
#     if request.method == 'POST':
#         user.delete()
#         return Response({'message':'탈퇴 성공'}, status=status.HTTP_202_ACCEPTED)
        

### 마이페이지, 회원 정보 조회, 회원 탈퇴

@api_view(['GET', 'DELETE'])
@login_required
def mypage(request):
    user = request.user
    if request.method == 'GET':
        serializer = UserInfoSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        user.delete()
        return Response({'message':'탈퇴 성공'}, status=status.HTTP_202_ACCEPTED)
    
@api_view(['GET'])
@login_required
def mypage_recom(request):
    user = request.user
    if request.method == 'GET':
        movies_df = load_movie_data(r"C:\Users\lyw\Desktop\SF12_Feelm\pjt_movie\django-pjt\movies\fixtures\movietop1.json")
        
        # 리뷰 평점 기반 추천
        user_reviews = user.reviews.values('movie_id', 'rating')
        movie_id = []
        tmdb_id = []
        rating = []
        for review in user_reviews:
            movie_id.append(review['movie_id']-1)
            rating.append(review['rating'])
            tmdb = Movie.objects.get(id=review['movie_id'])
            tmdb_id.append(tmdb)
        # print(movie_id)
        rating_df = pd.DataFrame({
            'movie_id':movie_id,
            'tmdb_id':tmdb_id,
            'rating':rating,
        })
        # print(rating_df[['movie_id']])

        if rating_df.empty:
            # rating_rec = movies_df.nlargest(20, 'vote_avg')[['tmdb_id', 'title']]
            rating_rec = movies_df[movies_df['vote_avg'] >= 7].sample(n=20)[['tmdb_id', 'title']]
            rating_recom = Movie.objects.filter(tmdb_id__in=rating_rec['tmdb_id'].tolist())
        else:
            rating_rec = movie_recommendation_system_combined_rating(
                r"C:\Users\lyw\Desktop\SF12_Feelm\pjt_movie\django-pjt\movies\fixtures\movietop1.json",
                rating_df,
                'title', 'overview', 'production_com', 'original_lang', 'genre', 'keyword', 
                4, 4, 1, 1, 3, 2.5, 
                20
            )
            rating_recom = Movie.objects.filter(tmdb_id__in=rating_rec)
        # print(rating_recom)
        # 북마크 기반 추천
        bookmark_list = list(request.user.bookmark.all().values())
        # print(bookmark_list)
        # DataFrame 생성
        bookmark = pd.DataFrame(bookmark_list)

        if bookmark.empty:
            movies_rec = movies_df[movies_df['vote_avg'] >= 7].sample(n=20)[['tmdb_id', 'title']]
            movies_recom = Movie.objects.filter(tmdb_id__in=movies_rec['tmdb_id'].tolist())
        else:
            movies_rec = movie_recommendation_system_combined_bookmark(
                r"C:\Users\lyw\Desktop\SF12_Feelm\pjt_movie\django-pjt\movies\fixtures\movietop1.json", 
                bookmark, 
                'title', 'overview', 'production_com', 'original_lang', 'genre', 'keyword', 
                5, 2, 1, 3, 4, 4, 
                20
            )
            movies_recom = Movie.objects.filter(tmdb_id__in=movies_rec)
            

        # print(serializer_bookmark.data)
        
        serializer_bookmark = MovieListSerializer(movies_recom, many=True)
        serializer_rating = MovieListSerializer(rating_recom, many=True)
        return Response({'review_recommendations':serializer_rating.data, 'bookmark_reccomendations': serializer_bookmark.data})
        # return Response(serializer_bookmark.data)
        

# 일기 목록, 작성
@api_view(['GET', 'POST'])
@login_required
def diary(request):
    user = request.user
    if request.method == 'GET':
        diaries = Diary.objects.filter(user=user)
        serializer = DiaryListSerializer(diaries, many=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'POST':
        tmdb_id = request.data['tmdb_id']
        movie = get_object_or_404(Movie, tmdb_id=tmdb_id)
        serializer = DiarySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

# 일기 상세보기, 수정, 삭제
@api_view(['GET', 'PUT', 'DELETE'])
@login_required
def diary_update(request, diary_id):
    user = request.user
    diary = get_object_or_404(Diary, id=diary_id)
    if request.method == 'GET':
        if user == diary.user:
            serializer = DiarySerializer(diary)
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        if user == diary.user:
            serializer = DiarySerializer(diary, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'DELETE':
        if user == diary.user:
            diary.delete()
            return Response({'message':'삭제 성공'}, status=status.HTTP_202_ACCEPTED)