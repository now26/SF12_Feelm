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
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly

from .serializers import MovieSerializer, MovieListSerializer
from .models import Movie




# # Create your views here.

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
# @permission_classes([IsAuthenticated])
# @permission_classes([JWTAuthentication])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def movie_detail(request, tmdb_id):
    movie = get_object_or_404(Movie, tmdb_id=tmdb_id)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        print(serializer.data)
        return Response(serializer.data)


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
