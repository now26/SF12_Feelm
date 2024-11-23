from django.urls import path
from . import views

urlpatterns = [
    # path('articles/', views.article_list),
    # path('articles/<int:article_pk>', views.article_detail),

    path('', views.article_list),
    path('<int:article_pk>/', views.article_detail),
]
