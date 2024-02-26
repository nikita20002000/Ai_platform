from django.urls import path
from . import views

from .views import RegisterView

urlpatterns = [
    path('', views.index, name='home'),
    path('profile/', views.profile, name='profile'),
    # path('register', views.register, name='register'),
    path('register', RegisterView.as_view(), name='register'),
]
