
from django.urls import include,path
from product import views

urlpatterns = [
    path('Detail', views.gallery),
    path('Shop-detail', views.shop_detail),
]
