from django.urls import path
from . import views

app_name = 'feelm'

urlpatterns = [
  # # 로그인 전 메인 화면
  # path('', views.index, name='index'),
  # # 로그인 후 메인 화면
  # path('movies/', views.movie_list, name='main'),


  # 로그인 후 메인 화면
  path('genre/', views.genre, name='genre'),

  # movie_list화면
  path('', views.movie_list, name='movie_list'),

  # movie_detail화면
  path('<int:tmdb_id>/', views.movie_detail, name='movie_detail'),
  
  # movie 좋아요
  path('<int:tmdb_id>/like/', views.like_movie, name='like_movie'),
  
  # movie 나중에 다시 볼 어쩌구
  path('<int:tmdb_id>/bookmark/', views.bookmark, name='bookmark'),
  
  # 리뷰 수정, 삭제
  path('<int:tmdb_id>/<int:review_id>/', views.review, name='review'),
  
  # 리뷰 좋아요
  path('<int:tmdb_id>/<int:review_id>/like/', views.like, name='like'),

  # path('tmdb/popular/', views.tmdb_popular, name='tmdb_popular'),
]