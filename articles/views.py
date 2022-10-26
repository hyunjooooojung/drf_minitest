from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import APIView
from rest_framework.generics import get_object_or_404
from articles import serializers
from articles.models import Article
from articles.serializers import ArticleSerializer

# Create your views here.
# 함수형 - 내가 한것.
# @api_view(['GET', 'POST'])
# def index(request):
#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ArticleSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
# 클래스형
# class Article(APIView):
#     def get(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = ArticleSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# 정답
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from articles.models import Article
from articles.serializers import ArticleSerializer

# 함수형 view
@api_view(['GET', 'POST'])
def index(request):
    # get 요청에 대한 처리
    if request.method == 'GET':
        print('get!!')
        return Response({'message': 'get success!!'})
        
    # post 요청에 대한 처리
    if request.method == 'POST':
        print('post!!')
        return Response({'message': 'post success!!'})

# 클래스형 view
class ArticleView(APIView):
    # get 요청에 대한 처리
    def get(self, request):
        all_articles = Article.objects.all()
        return Response(ArticleSerializer(all_articles, many=True).data)
        
    # post 요청에 대한 처리
    def post(self, request):
        article = ArticleSerializer(data=request.data)
        # 검증
        article.is_valid(raise_exception=True) # 검증 단계에서 문제가 있을 경우 에러 발생
        # 생성
        article.save() # 검증 단계에서 문제가 없을 경우 데이터 저장
        
        return Response(article.data)