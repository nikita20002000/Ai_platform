from django.urls import path, include
from .import views

app_name = "finance"
urlpatterns = [
    path('', views.finance_home, name='finance_home'),
    path('visualize', views.visualize, name='visualize'),
]