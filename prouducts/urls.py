from django.urls import path
from .views import items_list,itemsDetail


app_name='prouducts'


urlpatterns = [
    path('',items_list.as_view(),name='items_list'),
    path('<int:pk>',itemsDetail.as_view(),name='items_detail'),
 ]