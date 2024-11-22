from django.urls import path
from .views import SignupAPIView, LoginAPIView, LogoutView

# JWT 토큰(+ 241120)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignupAPIView.as_view(), name='signup'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # urls.py에 JWT 토큰을 발급받고 검증하는 API 엔드포인트를 추가
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # /api/token/: 로그인 시 사용자 정보를 바탕으로 JWT 액세스 토큰과 리프레시 토큰을 발급받을 수 있는 엔드포인트
    # /api/token/refresh/: 리프레시 토큰을 이용해 액세스 토큰을 갱신할 수 있는 엔드포인트

]
