from django.urls import path
from .views import SignupAPIView, LoginAPIView, LogoutView, UserRetrieveUpdateAPIView
from . import views

# JWT 토큰(+ 241120)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignupAPIView.as_view(), name='signup'),
    # username 중복확인
    path('check-username/', views.check_username, name='check-username'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # 회원정보 변경
    path('update/', UserRetrieveUpdateAPIView.as_view(), name='update'),
    # 회원탈퇴
    # path('delete/', views.delete, name='delete'),

    # urls.py에 JWT 토큰을 발급받고 검증하는 API 엔드포인트를 추가
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # mypage
    path('mypage/', views.mypage, name='mypage'),
    # mypage에서 내 정보 기반으로 영화 추천 //북마크 기반
    path('mypage/recom1/', views.mypage_recom1, name='mypage_recom1'),
    # mypage에서 내 정보 기반으로 영화 추천 //리뷰 기반
    path('mypage/recom2/', views.mypage_recom2, name='mypage_recom2'),
    
    # 일기쓰기
    path('mypage/diary/', views.diary, name='diary'),
    # 일기 수정, 삭제
    path('mypage/diary/<int:diary_id>/', views.diary_update, name='diary_id'),

    # /api/token/: 로그인 시 사용자 정보를 바탕으로 JWT 액세스 토큰과 리프레시 토큰을 발급받을 수 있는 엔드포인트
    # /api/token/refresh/: 리프레시 토큰을 이용해 액세스 토큰을 갱신할 수 있는 엔드포인트

]
