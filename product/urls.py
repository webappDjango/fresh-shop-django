
from django.urls import include,path
from product import views

urlpatterns = [
    path('Gallery', views.gallery),
    path('Shop-detail', views.shop_detail),
]
