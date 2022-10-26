from django.urls import path,include
from  articles import views

urlpatterns = [
    # 함수형 view 지정
    path('', views.index, name='index'),
    # 클래스형 view 지정
    # path('', views.ArticleView.as_view()),
]
