from django.contrib import admin
from django.urls import path, include

app_name = "web_app"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('accounts/', include("django.contrib.auth.urls"))
]
