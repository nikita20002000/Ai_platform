from django.urls import path, include
from . import views


app_name = "news"

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('search/', views.get_news_with_topic, name='search_news')
]
