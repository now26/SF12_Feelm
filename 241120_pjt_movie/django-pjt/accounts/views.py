from django.shortcuts import redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from rest_framework import status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import SignupSerializer, LoginSerializer, UserInfoSerializer
from .renders import UserJSONRenderer

# 회원가입
class SignupAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = SignupSerializer
    # renderer_classes = (UserJSONRenderer,) # pprint와 비슷한 기능
    
    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # 잘 뜨는지 로그인 창으로 리다이렉트 시키기
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
# 로그인
class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    # renderer_classes = (UserJSONRenderer,) # pprint와 비슷한 기능
    serializer_class = LoginSerializer

    def post(self, request):
        # 사용자 정보 가져오기
        username = request.data['username']

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        
        # 로그인 처리
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            login(request, user)

            # JWT 토큰 생성
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)
            # access_token = serializer.validated_data['access_token']
            # refresh_token = serializer.validated_data['refresh_token']
            return Response({
                'access_token': access_token,
                'refresh_token': refresh_token,
            }, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        


# 로그아웃
class LogoutView(APIView):
    # authentication_classes = [SessionAuthentication]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user:
            logout(request)
            return Response({'message':'로그아웃 완료'}, status=status.HTTP_202_ACCEPTED)
