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
    release_date = models.DateTimeField(null=True, blank=True)
    runtime = models.IntegerField(null=True, blank=True)
    adult = models.BooleanField(null=True, blank=True)
    movie_homepage = models.CharField(max_length=255, null=True, blank=True)
    backdrop_image = models.CharField(max_length=255, null=True, blank=True)
    production_com = models.CharField(max_length=255, null=True, blank=True)
    original_lang = models.CharField(max_length=20, null=True, blank=True)
    genre = models.TextField(null=True, blank=True)
    keyword = models.TextField(null=True, blank=True)
    spoken_lang = models.CharField(max_length=20, null=True, blank=True)


    like_movies = models.ManyToManyField('accounts.User', related_name='like_movies', null=True, blank=True)
    bookmark = models.ManyToManyField('accounts.User', related_name='bookmark', null=True, blank=True)

    def save(self, *args, **kwargs):
        # release_date가 naive datetime이면 timezone-aware datetime으로 변환
        if self.release_date and timezone.is_naive(self.release_date):
            self.release_date = timezone.make_aware(self.release_date, timezone.get_current_timezone())

        # 부모 클래스의 save 메서드 호출
        super(Movie, self).save(*args, **kwargs)


    # 이미지 상대경로 -> 절대경로 변경
    def get_full_poster_url(self, image_size="original"):
        # """포스터 이미지 URL을 반환, 기본 크기는 original."""
        base_url = "https://image.tmdb.org/t/p/" # 이미지 URL의 기본 경로
        # image_size = "w500"
        if self.poster_path: 
            return f"{base_url}{image_size}{self.poster_path}" # poster_path에 기본 URL을 추가
        else:
            return None # poster_path가 없다면 None 반환
    
    def get_full_backdrop_url(self, image_size = "original"):
        """배경 이미지 URL을 반환, 기본 크기는 original."""
        base_url = "https://image.tmdb.org/t/p/"
        # image_size = "original" 
        if self.backdrop_image:
            return f"{base_url}{image_size}{self.backdrop_image}"  # backdrop_image에 기본 URL을 추가
        else:
            return None # backdrop_image가 없다면 None 반환
        
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
    like_reviews = models.ManyToManyField('accounts.User', related_name='like_reviews', null=True, blank=True)
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