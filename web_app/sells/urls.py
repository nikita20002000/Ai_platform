from django.urls import path, include
from .views import SellsList, SellDetail, SellCreate, SellUpdate, DeleteSell

app_name = 'sells'

urlpatterns = [
    path('', SellsList.as_view(), name='sells-list'),
    path('sell/<int:pk>/', SellDetail.as_view(), name='sell'),
    path('sell-create/', SellCreate.as_view(), name='sell-create'),
    path('sell-update/<int:pk>/', SellUpdate.as_view(), name='sell-update'),
    path('sell-delete/<int:pk>/', DeleteSell.as_view(), name='sell-delete'),

]