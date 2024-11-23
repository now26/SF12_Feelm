from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
  poster_url = serializers.SerializerMethodField()
  backdrop_url = serializers.SerializerMethodField()

  class Meta:
    model = Movie
    fields = '__all__'
    
  def get_poster_url(self, obj):
    return obj.get_full_poster_url() # poster_path를 절대 URL로 반환
  
  def get_backdrop_url(self, obj):
    return obj.get_full_backdrop_url() # backdrop_image를 절대 URL로 반환



class MovieListSerializer(serializers.ModelSerializer):
  poster_url = serializers.SerializerMethodField()
  backdrop_url = serializers.SerializerMethodField()

  class Meta:
    model = Movie
    fields = ('tmdb_id', 'title', 'vote_avg', 'vote_count', 'status', 'release_date', 'runtime', 'poster_url', 'backdrop_url')
    

  def get_poster_url(self, obj):
    return obj.get_full_poster_url() # poster_path를 절대 URL로 반환
  
  def get_backdrop_url(self, obj):
    return obj.get_full_backdrop_url() # backdrop_image를 절대 URL로 반환