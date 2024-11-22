from rest_framework import serializers
from .models import Movie, Review

# 리뷰 시리얼라이저
class ReviewSerializer(serializers.ModelSerializer): 
  class Meta:
    model = Review
    fields = '__all__'
    read_only_fields = (
      'user',
      'movie'
    )


class MovieSerializer(serializers.ModelSerializer):
  poster_url = serializers.SerializerMethodField()
  backdrop_url = serializers.SerializerMethodField()
  reviews = ReviewSerializer(many=True, read_only=True, source='reviews.all')

  # 리뷰 보이기
  # class ReviewSerializer(serializers.ModelSerializer):
  #   class Meta:
  #     model = Review
  #     fields = '__all__'
    
  # review_set = ReviewSerializer(read_only=True, many=True)

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

  # 리뷰 보이기
  # class ReviewSerializer(serializers.ModelSerializer):
  #   class Meta:
  #     model = Review
  #     fields = '__all__'

  review_set = ReviewSerializer(read_only=True, many=True, source='reviews.all')
  review_count = serializers.IntegerField(source='review_set.count', read_only=True)

  class Meta:
    model = Movie
    fields = ('tmdb_id', 'title', 'vote_avg', 'vote_count', 'status', 'release_date', 'runtime', 'poster_url', 'backdrop_url')
    

  def get_poster_url(self, obj):
    return obj.get_full_poster_url() # poster_path를 절대 URL로 반환
  
  def get_backdrop_url(self, obj):
    return obj.get_full_backdrop_url() # backdrop_image를 절대 URL로 반환