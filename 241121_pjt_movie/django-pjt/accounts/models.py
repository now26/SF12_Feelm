import jwt, uuid
from datetime import datetime, timedelta, timezone
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models.fields import BooleanField

from .managers import UserManager
from movies.models import Movie

# 방법2. 닉네임 랜덤값 생성코드 추가
import random
import string

def generate_random_nickname():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))  # 8글자 길이의 랜덤 문자열 생성
# =========================================


def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return 'user_{0}/{1}'.format(instance.username, filename)

class User(AbstractBaseUser, PermissionsMixin):
    class GenderChoices(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
        PREFER_NOT_TO_SAY = 'N', 'Prefer not to say'
        
    username = models.CharField(max_length=200, unique=True)
    
    # 닉네임 랜덤 생성 함수 활용
    nickname = models.CharField(max_length=20, unique=True, default=generate_random_nickname)
    
    profile_image = models.ImageField(null=True, blank=True, upload_to=user_directory_path)
    gender = models.CharField(max_length=1, choices=GenderChoices.choices, default=GenderChoices.PREFER_NOT_TO_SAY,)
    age = models.PositiveIntegerField(default=20)
    is_active = BooleanField(default=True)
    is_staff = BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = (
        'nickname',
        'gender',
        'age',
    )
    objects = UserManager()
    
    def __str__(self):
        return self.username
    def get_full_name(self):
        return self.nickname
    
    # @property
    # def token(self):
    #     return self._generate_jwt_token()
    
    # def _generate_jwt_token(self):
    #     dt = datetime.now(timezone.utc) + timedelta(days=60)
    #     token = jwt.encode(
    #         {
    #             'id' : self.pk,
    #             'exp':dt.timestamp(),
    #         },
    #         settings.SECRET_KEY,
    #         algorithm='HS256'
    #     )
    #     return token
    
class Diary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='diary')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='diary')
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)