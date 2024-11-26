from django.contrib.auth.models import BaseUserManager

# 헬퍼 클래스
class UserManager(BaseUserManager):
    
    # 모든 유저에 대해
    def create_user(self, username, password=None, **extra_fields):
        if username is None:
            raise TypeError('Users must have a username.')
        if password is None:
            raise TypeError('Users must have a password.')
        
        user = self.model(
            username = username,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        
        return user
    
    def create_superuser(self, username, password, **extra_fields):
        if password is None:
            raise TypeError('Superuser must have a password.')
        
        user = self.create_user(username, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
    