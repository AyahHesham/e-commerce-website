from django.urls import path
from .views import items_list,itemsDetail,brand_list,brand_detail,category_list,postList
app_name='prouducts'
urlpatterns = [
    path('test',postList),
    path('',items_list.as_view(),name='items_list'),
    path('<int:pk>',itemsDetail.as_view(),name='items_detail'),
    path('brands/',brand_list.as_view(),name='brand_list'),
    path('brands/<int:pk>',brand_detail.as_view(),name='brand_detail'),
    path('cateogry/',category_list.as_view(),name='category_list'),
 ]