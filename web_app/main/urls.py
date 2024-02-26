from django.urls import path, include
from . import views
from .views import RegisterView, WebPasswordResetView, WebPasswordResetDone


app_name = "main"

urlpatterns = [
    path('', views.index, name='home'),
    path('profile/', views.profile, name='profile'),


    path('register/', RegisterView.as_view(), name='register'),
    path('password_reset/', WebPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', WebPasswordResetDone.as_view(), name='password_reset_done'),
]
