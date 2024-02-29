from django.urls import path, include
from .import views
from .views import RegisterView, WebPasswordResetView, WebPasswordResetDone, TaskList, image_upload_view


app_name = "main"

urlpatterns = [
    path('', TaskList.as_view(), name='home'),
    path('profile/', views.profile, name='profile'),


    path('register/', RegisterView.as_view(), name='register'),
    path('password_reset/', WebPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', WebPasswordResetDone.as_view(), name='password_reset_done'),

    path('upload/', views.image_upload_view, name='upload'),
]
