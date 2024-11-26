from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# from accounts.models import User

class Movie(models.Model):
    tmdb_id = models.IntegerField()
    poster_path = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    tagline = models.TextField(null=True, blank=True)
    overview = models.TextField(null=True, blank=True)
    vote_avg = models.FloatField(null=True, blank=True)
    vote_count = models.IntegerField(null=True, blank=True)
    # released == true    
    status = models.CharField(max_length=20, null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    runtime = models.IntegerField(null=True, blank=True)
    adult = models.BooleanField(null=True, blank=True)
    movie_homepage = models.CharField(max_length=255, null=True, blank=True)
    backdrop_image = models.CharField(max_length=255, null=True, blank=True)
    production_com = models.CharField(max_length=255, null=True, blank=True)
    original_lang = models.CharField(max_length=20, null=True, blank=True)
    genre = models.TextField(null=True, blank=True)
    keyword = models.TextField(null=True, blank=True)
    spoken_lang = models.CharField(max_length=20, null=True, blank=True)
    
    like_movies = models.ManyToManyField('accounts.User', related_name='like_movies')
    bookmark = models.ManyToManyField('accounts.User', related_name='bookmark')

     
    # image_size 참고
        # w300 – 300픽셀의 너비 (작은 사이즈)
        # w500 – 500픽셀의 너비
        # w780 – 780픽셀의 너비 (중간 사이즈)
        # w1280 – 1280픽셀의 너비 (큰 사이즈)
        # original – 원본 크기 (최대 해상도)

        # w1280이나 original 크기는 가장 큰 해상도를 제공하며, original은 이미지의 원본 크기 그대로 제공함.



# 리뷰 모델
class Review(models.Model):
    user = models.ForeignKey('accounts.User', related_name='reviews', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)
    content = models.TextField()
    like_reviews = models.ManyToManyField('accounts.User', related_name='like_reviews', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rating = models.FloatField(
        choices=[
            (0.0, '0'), (0.5, '0.5'), 
            (1.0, '1'), (1.5, '1.5'),
            (2.0, '2'), (2.5, '2.5'),
            (3.0, '3'), (3.5, '3.5'),
            (4.0, '4'), (4.5, '4.5'),
            (5.0, '5')
        ],
        default=0.0
    )