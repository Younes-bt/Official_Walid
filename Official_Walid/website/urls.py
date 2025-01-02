from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articles/<int:id>/', views.articles_view, name='articles'),
    path('create-article/', views.create_article, name='create_article'),
    path('create-video/', views.create_video, name='create_video'),
    path('allArticles/', views.allArticles, name='all_articles'),
    path('sendMessage/', views.send_message, name='send_message'),
]