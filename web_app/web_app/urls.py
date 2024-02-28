from django.contrib import admin
from django.urls import path, include

app_name = "web_app"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('to_do/', include('to_do_list.urls', namespace='to_do_list')),
    path('news/', include('news.urls', namespace='news')),
    path('accounts/', include("django.contrib.auth.urls")),
]
