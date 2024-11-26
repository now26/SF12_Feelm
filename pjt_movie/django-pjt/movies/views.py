import requests
from pprint import pprint

# from django.http import JsonResponse

from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# 인증 데코레이터
from rest_framework.decorators import authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication

# Permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny,IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly

from .serializers import MovieSerializer, MovieListSerializer, ReviewSerializer
from .models import Movie, Review

from accounts.models import User
from algo import movie_recommendation_system_combined, movie_recommendation_system_combined_bookmark


def index(request):
    pass

# 로그인 후 메인 화면
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @permission_classes([JWTAuthentication])
def main(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass

@api_view(['GET'])
# @permission_classes([AllowAny])
# @permission_classes([IsAuthenticated])
# @permission_classes([JWTAuthentication])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
    
@api_view(['GET', 'POST'])
def movie_detail(request, tmdb_id):
    user = request.user
    # movie = get_object_or_404(Movie, tmdb_id=tmdb_id)
    movie = Movie.objects.get(tmdb_id=tmdb_id)
    # review = Review.objects.filter(movie=movie.pk)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        print(movie.title)
        # 특정 영화 정보와 관련된 추천
        recommendations = movie_recommendation_system_combined(
            "C:/Users/SSAFY/Desktop/SF12_Feelm/pjt_movie/django-pjt/movies/fixtures/movietop1.json", 
            movie.title, 
            'title', 'production_com', 'original_lang', 'genre', 'keyword', 
            5, 1, 5, 3, 2, 
            20
        )
        print(recommendations)
        # if recommendations=="영화를 찾을 수 없습니다.":
        #     movies = None
        # else:
        movies = Movie.objects.filter(tmdb_id__in=recommendations)
        serializer_rec = MovieListSerializer(movies, many=True)
        # print(serializer_rec.data)
        return Response({'movie_detail':serializer.data, 'movie_recommend':serializer_rec.data})
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 리뷰 put, delete
@api_view(['PUT', 'DELETE'])
def review(request, tmdb_id, review_id):
    user = request.user
    movie = get_object_or_404(Movie, tmdb_id=tmdb_id)
    review = get_object_or_404(Review, id=review_id)
    if request.method == 'PUT':
        if user == review.user:
            serializer = ReviewSerializer(review, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response({'message':'본인이 작성한 리뷰가 아닙니다.'}, status=status.HTTP_401_UNAUTHORIZED)
    elif request.method == 'DELETE':
        print(review.user)
        if user == review.user:
            review.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response({'message':'본인이 작성한 리뷰가 아닙니다.'}, status=status.HTTP_401_UNAUTHORIZED)

# 영화 좋아요
@api_view(['POST'])
def like_movie(request, tmdb_id):
    user = request.user
    movie = get_object_or_404(Movie, tmdb_id=tmdb_id)
    if request.method == 'POST':
        # 유저가 좋아요 목록에 있다면 좋아요 취소
        if user in movie.like_movies.all():
            movie.like_movies.remove(user)
            return Response({'message':'좋아요 취소 성공'}, status=status.HTTP_202_ACCEPTED)
        # 유저가 좋아요 목록에 없다면 좋아요 추가
        else:
            movie.like_movies.add(user)
            return Response({'message':'좋아요 성공'}, status=status.HTTP_202_ACCEPTED)

# 영화 북마크
@api_view(['POST'])
def bookmark(request, tmdb_id):
    user = request.user
    movie = get_object_or_404(Movie, tmdb_id=tmdb_id)
    if request.method == 'POST':
        # 유저가 북마크 목록에 있다면 북마크 취소
        if user in movie.bookmark.all():
            movie.bookmark.remove(user)
            return Response({'message':'북마크 취소 성공'}, status=status.HTTP_202_ACCEPTED)
        # 유저가 북마크 목록에 없다면 북마크 추가
        else:
            movie.bookmark.add(user)
            return Response({'message':'북마크 성공'}, status=status.HTTP_202_ACCEPTED)


# 리뷰 좋아요
@api_view(['POST'])
def like(request, tmdb_id, review_id):
    user = request.user
    movie = get_object_or_404(Movie, tmdb_id=tmdb_id)
    review = get_object_or_404(Review, id=review_id)
    if request.method == 'POST':
        # 유저가 좋아요 목록에 있다면 좋아요 취소
        if user in review.like_reviews.all():
            review.like_reviews.remove(user)
            return Response({'message':'좋아요 취소 성공'}, status=status.HTTP_202_ACCEPTED)
        # 유저가 좋아요 목록에 없다면 좋아요 추가
        else:
            review.like_reviews.add(user)
            return Response({'message':'좋아요 성공'}, status=status.HTTP_202_ACCEPTED)
        


# # TMDB API에서 데이터 다운로드 후 출력
# @api_view(['GET'])
# def tmdb_popular(request):
#     # api_key_t = "87246d75e1ce26e1392a087b3d1d88c5"
#     # api_key = "25b62afd0ef2a3701ce5233b6515b501"
#     tmdb_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNWI2MmFmZDBlZjJhMzcwMWNlNTIzM2I2NTE1YjUwMSIsIm5iZiI6MTczMjE3MDM4OC4wODMyMDc2LCJzdWIiOiI2NzIwNjczZjZkNmI3MDVkYzg3MjEwNDAiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.iiaEIB3EVXs44t7jFBqY2ZmMZvotTi4fUxxl-2mPSQU"

#     option = 'popular'
#     language = 'en-US'
#     page_num = 1

#     tmdb_url = f"https://api.themoviedb.org/3/movie/{option}?language={language}&page={page_num}"

#     headers = {
#         # "accept": "application/json",
#         "Authorization": f"Bearer {tmdb_token}"
#     }
#     response = requests.get(tmdb_url, headers=headers)
#     data = response.json()
#     return Response(data)
