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

# 추천 알고리즘
import pandas as pd
import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# JSON 파일 로드
def load_movie_data(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    # fields 부분만 추출하여 DataFrame 생성
    movies_df = pd.DataFrame([item['fields'] for item in data])
    return movies_df

# 추천 알고리즘
def calculate_combined_weighted_similarity(movies_df, field1, field2, field3, field4, field5, field6, weight1, weight2, weight3, weight4, weight5, weight6):
    # 장르와 키워드를 결합
    combined_features = movies_df.apply(
        lambda row: "{} ".format(' '.join([row[field1]] * int(weight1))) + 
        "{} ".format(' '.join([row[field2]] * int(weight2))) +
        "{} ".format(' '.join([row[field3]] * int(weight3))) +
        "{} ".format(' '.join([row[field4]] * int(weight4))) +
        "{} ".format(' '.join([row[field5]] * int(weight5))) +
        "{}".format(' '.join([row[field6]] * int(weight6))), axis=1)
    
    count_vect = CountVectorizer(min_df=1, ngram_range=(1, 2))
    combined_mat = count_vect.fit_transform(combined_features)
    
    # 코사인 유사도 계산
    combined_sim = cosine_similarity(combined_mat, combined_mat)
    return combined_sim

def find_sim_movie_combined(df, sorted_ind, title_name, top_n=10):
    # 입력된 영화의 인덱스 찾기
    title_movie = df[df['title'] == title_name]
    if title_movie.empty:
        return "영화를 찾을 수 없습니다."
    
    title_index = title_movie.index.values
    
    # 유사도 높은 영화 인덱스 추출
    similar_indexes = sorted_ind[title_index, :(top_n*2)]
    similar_indexes = similar_indexes.reshape(-1)
    
    # 입력 영화 제외
    similar_indexes = similar_indexes[similar_indexes != title_index]
    
    # 유사도 순으로 정렬, 슬라이싱
    result = df.iloc[similar_indexes][:top_n]
    # return result[['title', 'genre', 'vote_avg', 'overview', 'keyword']]
    return list(result[['tmdb_id'][0]])


def movie_recommendation_system_combined(json_file_path, title_name, key1, key2, key3, key4, key5, key6, weight1, weight2, weight3, weight4, weight5, weight6, top_n=10):
    # 데이터 로드
    movies_df = load_movie_data(json_file_path)
    # print(movies_df)
    
    # 유사도 계산
    combined_sim = calculate_combined_weighted_similarity(movies_df, key1, key2, key3, key4, key5, key6, weight1, weight2, weight3, weight4, weight5, weight6)
    
    # 유사도 정렬
    combined_sim_sorted_ind = combined_sim.argsort()[:, ::-1]
    
    # 추천 영화 찾기
    recommendations = find_sim_movie_combined(movies_df, combined_sim_sorted_ind, title_name, top_n)

    
    return recommendations

# ============================================
# 북마크 기반 추천
def calculate_combined_weighted_similarity_bookmark(movies_df, bookmark, field1, field2, field3, field4, field5, field6, weight1, weight2, weight3, weight4, weight5, weight6):
    bookmark = pd.DataFrame(bookmark)
    
    combined_bookmark = bookmark.apply(
        lambda row: "{} ".format(' '.join([row[field1]] * int(weight1))) + 
        "{} ".format(' '.join([row[field2]] * int(weight2))) +
        "{} ".format(' '.join([row[field3]] * int(weight3))) +
        "{} ".format(' '.join([row[field4]] * int(weight4))) +
        "{} ".format(' '.join([row[field5]] * int(weight5))) +
        "{}".format(' '.join([row[field6]] * int(weight6))), axis=1
    )
    # 장르와 키워드를 결합
    combined_features = movies_df.apply(
        lambda row: "{} ".format(' '.join([row[field1]] * int(weight1))) + 
        "{} ".format(' '.join([row[field2]] * int(weight2))) +
        "{} ".format(' '.join([row[field3]] * int(weight3))) +
        "{} ".format(' '.join([row[field4]] * int(weight4))) +
        "{} ".format(' '.join([row[field5]] * int(weight5))) +
        "{}".format(' '.join([row[field6]] * int(weight6))), axis=1)
    
    combined_features = pd.concat([combined_features, combined_bookmark], ignore_index=True)
    count_vect = CountVectorizer(min_df=1, ngram_range=(1, 2))
    combined_mat = count_vect.fit_transform(combined_features)
    
    # 코사인 유사도 계산
    combined_sim = cosine_similarity(combined_mat, combined_mat)
    return combined_sim

def find_sim_movie_combined_bookmark(df, sorted_ind, bookmark, top_n=10):
    # 입력된 영화의 인덱스 찾기
    title_movie = pd.DataFrame(bookmark)
    
    title_index = len(df)
    
    # 유사도 높은 영화 인덱스 추출
    similar_indexes = sorted_ind[title_index, :(top_n*2)]
    similar_indexes = similar_indexes.reshape(-1)
    
    # 입력 영화 제외
    similar_indexes = similar_indexes[similar_indexes != title_index]
    similar_indexes = similar_indexes[similar_indexes < title_index]
    
    # 유사도 순으로 정렬, 슬라이싱
    result = df.iloc[similar_indexes][:top_n]
    # return result[['title', 'genre', 'vote_avg', 'overview', 'keyword']]
    return list(result[['tmdb_id'][0]])

def movie_recommendation_system_combined_bookmark(json_file_path, bookmark, key1, key2, key3, key4, key5, key6, weight1, weight2, weight3, weight4, weight5, weight6, top_n=10):
    # 데이터 로드
    movies_df = load_movie_data(json_file_path)
    # print(movies_df)
    
    # 유사도 계산
    combined_sim = calculate_combined_weighted_similarity_bookmark(movies_df, bookmark, key1, key2, key3, key4, key5, key6, weight1, weight2, weight3, weight4, weight5, weight6)
    
    # 유사도 정렬
    combined_sim_sorted_ind = combined_sim.argsort()[:, ::-1]
    
    # 추천 영화 찾기
    recommendations = find_sim_movie_combined_bookmark(movies_df, combined_sim_sorted_ind, bookmark, top_n)

    
    return recommendations

# =============================================

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
        # bookmark = pd.DataFrame(list(request.user.bookmark.all().values()))
        # bookmark_list = list(request.user.bookmark.all().values())
        # DataFrame 생성
        # bookmark = pd.DataFrame(bookmark_list)
        # print(bookmark)
        # movies_rec = movie_recommendation_system_combined_bookmark("C:/Users/SSAFY/Desktop/새 폴더 (4)/SF12_Feelm/pjt_movie/django-pjt/movies/fixtures/moviepopular.json", bookmark, 'title', 'overview', 'production_com', 'original_lang', 'genre', 'keyword', 2, 1, 1, 2, 1.8, 1.8, 10)
        # movies_recom = Movie.objects.filter(tmdb_id__in=movies_rec)
        # serializer_bookmark = MovieListSerializer(movies_recom, many=True)
        return Response(serializer.data)
    
@api_view(['GET', 'POST'])
def movie_detail(request, tmdb_id):
    user = request.user
    movie = get_object_or_404(Movie, tmdb_id=tmdb_id)
    # review = Review.objects.filter(movie=movie.pk)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        
        # 특정 영화 정보와 관련된 추천
        recommendations = movie_recommendation_system_combined("C:/Users/SSAFY/Desktop/새 폴더 (4)/SF12_Feelm/pjt_movie/django-pjt/movies/fixtures/moviepopular.json", movie.title, 'title', 'overview', 'production_com', 'original_lang', 'genre', 'keyword', 2, 1, 1, 2, 1.8, 1.8, 10)
        movies = Movie.objects.filter(tmdb_id__in=recommendations)
        serializer_rec = MovieListSerializer(movies, many=True)
        print(serializer_rec.data)
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
