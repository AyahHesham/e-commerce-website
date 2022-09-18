from django.urls import path
from .views import items_list,itemsDetail

 
urlpatterns = [
    path('',items_list.as_view(),name='prouducts_list'),
    path('<int:pk>',itemsDetail.as_view(),name='prouducts_list'),
 ]