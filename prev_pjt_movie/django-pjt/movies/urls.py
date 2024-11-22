from django.urls import path
from . import views

app_name = 'feelm'

urlpatterns = [
  # # 로그인 전 메인 화면
  # path('', views.index, name='index'),
  # # 로그인 후 메인 화면
  # path('movies/', views.movie_list, name='main'),


  # 로그인 후 메인 화면
  # path('', views.main, name='main'),

  # movie_list화면
  path('', views.movie_list, name='movie_list'),

  # movie_detail화면
  path('<int:tmdb_id>/', views.movie_detail, name='movie_detail'),

  # path('tmdb/popular/', views.tmdb_popular, name='tmdb_popular'),
]