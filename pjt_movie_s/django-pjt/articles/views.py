# Create your views here.
from django.shortcuts import render

# 조회 쿼리셋
from django.shortcuts import get_list_or_404, get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# 인증 데코레이터
from rest_framework.decorators import authentication_classes
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializers import ArticleListSerializer, ArticleSerializer
from .models import Article


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@permission_classes([JWTAuthentication])
# @permission_classes([IsAdminUser])
# @authentication_classes([TokenAuthentication, BasicAuthentication])
def article_list(request):
  if request.method == 'GET':
    articles = get_list_or_404(Article)
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)
  
  elif request.method == 'POST':
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      # serializer.save()

      # user 정보 저장
      serializer.save(user = request.user)
      return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def article_detail(request, article_pk):
  article = get_object_or_404(Article, pk=article_pk)
  
  if request.method == 'GET':
    serializer = ArticleSerializer(article)
    print(serializer.data)
    return Response(serializer.data)