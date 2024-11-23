from django.shortcuts import redirect, get_list_or_404, get_object_or_404
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
from rest_framework.generics import RetrieveUpdateAPIView

from .models import User, Diary
from .serializers import SignupSerializer, LoginSerializer, UserInfoSerializer, DiarySerializer, DiaryListSerializer, UserSerializer
from .renders import UserJSONRenderer

from movies.models import Movie, Review

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

# 회원정보 변경
class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    
    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
# 회원탈퇴
# @api_view(['POST'])
# @login_required
# def delete(request):
#     user = request.user
#     if request.method == 'POST':
#         user.delete()
#         return Response({'message':'탈퇴 성공'}, status=status.HTTP_202_ACCEPTED)
        

### 마이페이지, 회원 정보 조회, 회원 탈퇴
@api_view(['GET', 'DELETE'])
@login_required
def mypage(request):
    user = request.user
    if request.method == 'GET':
        serializer = UserInfoSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        user.delete()
        return Response({'message':'탈퇴 성공'}, status=status.HTTP_202_ACCEPTED)
    
# 일기 목록, 작성
@api_view(['GET', 'POST'])
@login_required
def diary(request):
    user = request.user
    if request.method == 'GET':
        diaries = Diary.objects.filter(user=user)
        serializer = DiaryListSerializer(diaries, many=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'POST':
        tmdb_id = request.data['tmdb_id']
        movie = get_object_or_404(Movie, tmdb_id=tmdb_id)
        serializer = DiarySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    
# 일기 수정, 삭제
@api_view(['PUT', 'DELETE'])
@login_required
def diary_update(request, diary_id):
    user = request.user
    diary = get_object_or_404(Diary, id=diary_id)
    if request.method == 'PUT':
        if user == diary.user:
            serializer = DiarySerializer(diary, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'DELETE':
        if user == diary.user:
            diary.delete()
            return Response({'message':'삭제 성공'}, status=status.HTTP_202_ACCEPTED)
    